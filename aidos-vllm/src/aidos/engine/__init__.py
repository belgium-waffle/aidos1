"""In-engine half of Aidos (vLLM V1).

  plugin.py    vLLM general-plugin entry point; patches GPUModelRunner (worker side)
  runner.py    worker side: aux capture, on-GPU scoring, bans, truncation, async readout
  scheduler.py engine-core side: policy, commit horizon, KV rollback, telemetry
  policy.py    pure-Python decision logic (no vLLM import; unit tested)
  compat.py    every touch-point with vLLM internals, in one place
  channel.py   side channel riding on SchedulerOutput / ModelRunnerOutput
  heads.py     loads trained heads, folds them into one weight bank
  factory.py   builds a vllm.LLM with or without Aidos
"""
