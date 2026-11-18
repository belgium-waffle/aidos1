#!/usr/bin/env bash
# OpenAI-compatible server with Aidos. The live view runs in a second terminal.
set -euo pipefail
aidos config bundles/qwen2.5-7b-instruct --lam 1 --retriever my_corpus.jsonl \
      --status aidos_status.json --telemetry aidos_telemetry.jsonl -o aidos_runtime.json
AIDOS_CONFIG="$PWD/aidos_runtime.json" vllm serve Qwen/Qwen2.5-7B-Instruct \
  --scheduler-cls aidos.engine.scheduler.AidosScheduler --no-async-scheduling --max-model-len 2048 &
aidos live --status aidos_status.json
