"""Closed-book QA data: loading, prompting, answer checking, splits.

Why short-form QA: correctness can be checked by alias matching, so every generated
token gets a reliable label without an LLM judge. That makes the probe's training signal
(and the benchmark's hallucination rate) cheap and reproducible.
"""

from __future__ import annotations

import json
import re
import string
from dataclasses import dataclass
from typing import Callable

from ..utils import stable_hash

SYSTEM_PROMPT = (
    "Answer the question with a short phrase only: a name, date, number, or short noun "
    "phrase. Do not explain."
)

# train: fit heads | val: layer choice, early stopping, Platt | cal: conformal threshold ONLY
# | test: report | ood: held-out datasets never seen by any fitting step.
# cal must not be touched by anything else, or the conformal guarantee breaks (the first
# 32B run reused one split for all four and got FAR 12.5% at alpha 10%).
SPLITS = ("train", "val", "cal", "test")
SPLIT_CODE = {s: i for i, s in enumerate((*SPLITS, "ood"))}


@dataclass
class QAItem:
    qid: str
    dataset: str
    question: str
    answers: list[str]


def _triviaqa(n: int, seed: int) -> list[QAItem]:
    from datasets import load_dataset

    ds = load_dataset("mandarjoshi/trivia_qa", "rc.nocontext", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n, len(ds))))
    out = []
    for r in ds:
        a = r["answer"]
        answers = sorted({*a["aliases"], *a["normalized_aliases"], a["value"]} - {""})
        out.append(QAItem(f"tqa-{r['question_id']}", "triviaqa", r["question"].strip(), answers))
    return out


def _popqa(n: int, seed: int) -> list[QAItem]:
    # long-tail entities -> much higher hallucination rate than TriviaQA
    from datasets import load_dataset

    ds = load_dataset("akariasai/PopQA", split="test")
    ds = ds.shuffle(seed=seed).select(range(min(n, len(ds))))
    out = []
    for r in ds:
        answers = json.loads(r["possible_answers"])
        out.append(QAItem(f"popqa-{r['id']}", "popqa", r["question"].strip(), sorted(set(answers))))
    return out


def _nq(n: int, seed: int) -> list[QAItem]:
    from datasets import load_dataset

    ds = load_dataset("google-research-datasets/nq_open", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n, len(ds))))
    out = []
    for r in ds:
        q = r["question"].strip()
        out.append(QAItem(f"nq-{stable_hash(q):x}", "nq", q, sorted(set(r["answer"]))))
    return out


def _sciq(n: int, seed: int) -> list[QAItem]:
    # science exam questions, asked closed-book (the multiple-choice options are dropped)
    from datasets import load_dataset

    ds = load_dataset("allenai/sciq", split="test")
    ds = ds.shuffle(seed=seed).select(range(min(n, len(ds))))
    out = []
    for r in ds:
        q = r["question"].strip()
        out.append(QAItem(f"sciq-{stable_hash(q):x}", "sciq", q, [r["correct_answer"].strip()]))
    return out


def _hotpotqa(n: int, seed: int) -> list[QAItem]:
    # multi-hop questions, asked closed-book; yes/no questions are skipped (alias matching
    # cannot tell a lucky guess from knowledge there)
    from datasets import load_dataset

    ds = load_dataset("hotpotqa/hotpot_qa", "distractor", split="validation")
    ds = ds.shuffle(seed=seed)
    out = []
    for r in ds:
        a = r["answer"].strip()
        if normalize_answer(a) in ("yes", "no") or not a:
            continue
        out.append(QAItem(f"hotpot-{r['id']}", "hotpotqa", r["question"].strip(), [a]))
        if len(out) >= n:
            break
    return out


def _twowiki(n: int, seed: int) -> list[QAItem]:
    # 2WikiMultihopQA (compositional / comparison / inference / bridge-comparison questions
    # over two Wikipedia articles), asked closed-book: the multi-hop OOD set. Adaptive-
    # retrieval methods that read internal states degrade on multi-hop (Moskvoretskii et
    # al., ACL 2025); this set tests whether Aidos does. Yes/no answers skipped.
    from datasets import load_dataset

    ds = load_dataset("framolfese/2WikiMultihopQA", split="validation")
    ds = ds.shuffle(seed=seed)
    out = []
    for r in ds:
        a = (r["answer"] or "").strip()
        if not a or normalize_answer(a) in ("yes", "no"):
            continue
        out.append(QAItem(f"2wiki-{r['id']}", "2wikimultihopqa", r["question"].strip(), [a]))
        if len(out) >= n:
            break
    return out


# ---- D19 fresh OOD sets (pre-registered 2026-11-14): never used by any earlier run, fitting step or analysis.
def _webquestions(n: int, seed: int) -> list[QAItem]:
    # Freebase questions from Google Suggest (Berant et al. 2013); test split only
    from datasets import load_dataset

    ds = load_dataset("Stanford/web_questions", split="test").shuffle(seed=seed)
    out = []
    for r in ds:
        answers = sorted({a.strip() for a in r["answers"]} - {""})
        if answers:
            q = r["question"].strip()
            out.append(QAItem(f"webq-{stable_hash(q):x}", "webquestions", q, answers))
        if len(out) >= n:
            break
    return out


def _musique(n: int, seed: int) -> list[QAItem]:
    # MuSiQue answerable (Trivedi et al. 2022): 2-4 hop composed questions, asked closed-book
    from datasets import load_dataset

    ds = load_dataset("dgslibisey/MuSiQue", split="validation").shuffle(seed=seed)
    out = []
    for r in ds:
        a = (r["answer"] or "").strip()
        if not r.get("answerable", True) or not a or normalize_answer(a) in ("yes", "no"):
            continue
        answers = sorted({a, *[x.strip() for x in (r.get("answer_aliases") or [])]} - {""})
        out.append(QAItem(f"musique-{r['id']}", "musique", r["question"].strip(), answers))
        if len(out) >= n:
            break
    return out


def _simpleqa(n: int, seed: int) -> list[QAItem]:
    # SimpleQA (Wei et al. 2024): short fact-seeking questions collected adversarially against GPT-4
    from datasets import load_dataset

    ds = load_dataset("basicv8vc/SimpleQA", split="test").shuffle(seed=seed)
    out = []
    for r in ds:
        a = (r["answer"] or "").strip()
        if not a:
            continue
        q = r["problem"].strip()
        out.append(QAItem(f"simpleqa-{stable_hash(q):x}", "simpleqa", q, [a]))
        if len(out) >= n:
            break
    return out


LOADERS: dict[str, Callable[[int, int], list[QAItem]]] = {
    "webquestions": _webquestions,
    "musique": _musique,
    "simpleqa": _simpleqa,
    "triviaqa": _triviaqa,
    "popqa": _popqa,
    "nq": _nq,
    "sciq": _sciq,
    "hotpotqa": _hotpotqa,
    "2wikimultihopqa": _twowiki,
}


def load_items(datasets: dict[str, int], seed: int, offsets: dict[str, int] | None = None) -> list[QAItem]:
    """n questions per dataset; offsets[name] skips the first questions of the same shuffled
    list (a sealed set disjoint from a run that drew offsets[name] with the same seed)."""
    items: list[QAItem] = []
    for name, n in datasets.items():
        if name not in LOADERS:
            raise KeyError(f"unknown dataset {name!r}; choose from {sorted(LOADERS)}")
        off = int((offsets or {}).get(name, 0))
        items.extend(LOADERS[name](off + int(n), seed)[off:])
    return items


def item_split(qid: str, dataset: str, fracs: list[float], ood: set[str] | dict, seed: int = 0) -> str:
    """Split of one question: every question of an OOD dataset is 'ood'."""
    return "ood" if dataset in ood else assign_split(qid, fracs, seed)


def assign_split(qid: str, fracs: list[float], seed: int = 0) -> str:
    """Deterministic question-level split. Splitting by question (never by token) keeps
    tokens of one answer from leaking between train and test."""
    if len(fracs) != len(SPLITS) or abs(sum(fracs) - 1) > 1e-6:
        raise ValueError(f"split_fracs must give {len(SPLITS)} fractions {SPLITS} summing to 1, got {fracs}")
    u = (stable_hash(f"{seed}:{qid}") % 100_000) / 100_000
    acc = 0.0
    for name, f in zip(SPLITS, fracs):
        acc += f
        if u < acc:
            return name
    return SPLITS[-1]


_PUNCT = set(string.punctuation)
_ARTICLES = re.compile(r"\b(a|an|the)\b")


def normalize_answer(s: str) -> str:
    """SQuAD-style normalization."""
    s = s.lower()
    s = "".join(ch for ch in s if ch not in _PUNCT)
    s = _ARTICLES.sub(" ", s)
    return " ".join(s.split())


def is_correct(pred: str, answers: list[str]) -> bool:
    """True if any normalized gold alias appears as a whole-word span of the prediction."""
    p = normalize_answer(pred)
    if not p:
        return False
    padded = f" {p} "
    for a in answers:
        na = normalize_answer(a)
        if na and f" {na} " in padded:
            return True
    return False


_ABSTAIN_PREFIXES = (
    "i dont know", "i do not know", "im not sure", "i am not sure", "unknown",
    "i cannot", "i cant", "sorry", "no answer", "not sure", "unsure",
)


def is_abstention(text: str) -> bool:
    t = normalize_answer(text)
    return (not t) or any(t.startswith(p) for p in _ABSTAIN_PREFIXES)


def build_messages(question: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]


def _merge_system(msgs):
    """For templates without a system role (Gemma, some Mistral versions): prepend the
    system text to the first user message."""
    if not msgs or msgs[0]["role"] != "system":
        return msgs
    sys_text, rest = msgs[0]["content"], [dict(m) for m in msgs[1:]]
    for m in rest:
        if m["role"] == "user":
            m["content"] = f"{sys_text}\n\n{m['content']}"
            break
    return rest


def _render(tokenizer, msgs, add_generation_prompt: bool, tokenize: bool):
    def call(m):
        try:  # Qwen3: disable the thinking block; Llama 3.x: fixed date in the system header
            # (its template stamps today's date otherwise, so prompts tokenized on different
            # days would differ); templates ignore kwargs they do not use
            return tokenizer.apply_chat_template(
                m, add_generation_prompt=add_generation_prompt, tokenize=tokenize, enable_thinking=False,
                date_string="26 Jul 2024"
            )
        except TypeError:
            return tokenizer.apply_chat_template(m, add_generation_prompt=add_generation_prompt, tokenize=tokenize)

    try:
        out = call(msgs)
    except Exception as e:  # jinja TemplateError: "system role not supported" and the like
        if msgs and msgs[0]["role"] == "system" and "TypeError" not in type(e).__name__:
            out = call(_merge_system(msgs))
        else:
            raise
    if hasattr(out, "keys"):  # BatchEncoding in newer transformers
        out = out["input_ids"]
    return out


def build_prompt_ids(tokenizer, question: str) -> list[int]:
    return [int(t) for t in _render(tokenizer, build_messages(question), True, True)]


# ------------------------------------------------------------------ retrieval turns
RAG_INSTRUCTION = (
    "Here is retrieved context that may help:\n\n{context}\n\n"
    "Using this context if it is relevant, answer the original question with a short phrase only."
)
_KEEP = "⁣KEEP⁣"  # invisible marker: where the kept (partial) assistant answer goes


def format_passages(passages: list[dict], max_chars: int = 600) -> str:
    lines = []
    for i, p in enumerate(passages, 1):
        title = p.get("title", "").strip()
        text = " ".join(p.get("text", "").split())[:max_chars]
        lines.append(f"[{i}] {title}: {text}" if title else f"[{i}] {text}")
    return "\n".join(lines)


def rag_insertion_ids(tokenizer, question: str, passages: list[dict], max_chars: int = 600) -> list[int]:
    """Tokens appended after the assistant's kept (possibly empty) partial answer to hand
    it retrieved evidence: <end of assistant turn> <user turn with context> <assistant header>.
    Built from the model's own chat template, so it works for any instruct model.

    The same tokens are used in the engine (mid-generation insertion) and offline (the RAG
    prompts of the sample stage): prompt + insertion == the conversation
    [system, user(q), assistant(""), user(context)] + generation prompt."""
    base = build_messages(question) + [{"role": "assistant", "content": _KEEP}]
    full = base + [{"role": "user", "content": RAG_INSTRUCTION.format(context=format_passages(passages, max_chars))}]
    text = _render(tokenizer, full, True, False)
    cut = text.index(_KEEP) + len(_KEEP)
    return [int(t) for t in tokenizer.encode(text[cut:], add_special_tokens=False)]


def build_rag_prompt_ids(tokenizer, question: str, passages: list[dict], max_chars: int = 600) -> list[int]:
    return build_prompt_ids(tokenizer, question) + rag_insertion_ids(tokenizer, question, passages, max_chars)


# ------------------------------------------------------------------- long-form turns
# Long-form prompts carry no system prompt: the long-form heads were trained on LongFact
# conversations rendered as a single user turn (pipeline/longform.py)
LF_CONTINUE = (
    "Here is retrieved context that may help:\n\n{context}\n\n"
    "Continue your previous answer exactly where it stopped, using this context where it is relevant "
    "and ignoring it where it is not. Do not start over, do not repeat what you already wrote, and do not "
    "mention the context."
)
LF_UPFRONT = "Here is retrieved context that may help:\n\n{context}\n\n{prompt}"


def build_lf_prompt_ids(tokenizer, prompt: str, passages: list[dict] | None = None, max_chars: int = 600) -> list[int]:
    """Long-form prompt; with passages, the always-retrieve (RAG up front) variant."""
    text = LF_UPFRONT.format(context=format_passages(passages, max_chars), prompt=prompt) if passages else prompt
    return [int(t) for t in _render(tokenizer, [{"role": "user", "content": text}], True, True)]


def lf_insertion_ids(tokenizer, prompt: str, passages: list[dict], max_chars: int = 600,
                     seed_ids: list[int] | None = None) -> list[int]:
    """Mid-answer evidence turn for long-form (lf-retrieve): <end of assistant turn> <user
    turn> <assistant header>. The client sees the released sentences followed by the
    continuation.

    seed_ids None ("turn"): the user turn is context + "continue where you stopped".
    seed_ids given ("seeded", D86): the user turn is FLARE's prompt (context, then the
    original prompt) and the new assistant turn opens with the answer so far (seed_ids), so
    the model continues its own sentence rather than starting a new reply."""
    ctx = format_passages(passages, max_chars)
    msg = LF_CONTINUE.format(context=ctx) if seed_ids is None else LF_UPFRONT.format(context=ctx, prompt=prompt)
    base = [{"role": "user", "content": prompt}, {"role": "assistant", "content": _KEEP}]
    text = _render(tokenizer, base + [{"role": "user", "content": msg}], True, False)
    cut = text.index(_KEEP) + len(_KEEP)
    return [int(t) for t in tokenizer.encode(text[cut:], add_special_tokens=False)] + [int(t) for t in seed_ids or []]


# ------------------------------------------------------------------- span labels
def first_error_token(tokenizer, answer_ids: list[int], answers: list[str]) -> int | None:
    """Index of the first answer token after which the answer can no longer become correct:
    the shortest prefix whose normalized text is not a prefix of any normalized gold alias
    (and does not already contain one). None if the answer is correct.

    This turns the answer-level label into a span-level one: tokens before the first error
    were still on a correct path, so they are not hallucinations."""
    golds = [g for g in (normalize_answer(a) for a in answers) if g]
    # paths that are still "on the way" to a gold answer: with or without a leading article
    # (normalization drops articles, but a partial "Th" is not yet the article "the")
    paths = set(golds)
    for a in answers:
        paths.add(_loose(a))
        for art in ("the ", "a ", "an "):
            paths.update(art + g for g in golds)
    paths.discard("")
    for j in range(1, len(answer_ids) + 1):
        text = tokenizer.decode(answer_ids[:j], skip_special_tokens=True)
        p = normalize_answer(text)
        if p and any(f" {g} " in f" {p} " for g in golds):
            return None  # correct from here on
        loose = _loose(text)
        if not loose:
            continue
        if not any(path.startswith(loose) or (p and path.startswith(p)) for path in paths):
            return j - 1
    return len(answer_ids) - 1 if answer_ids else None


def _loose(s: str) -> str:
    """Lowercase, punctuation stripped, whitespace collapsed; articles KEPT."""
    s = "".join(ch for ch in s.lower() if ch not in _PUNCT)
    return " ".join(s.split())
