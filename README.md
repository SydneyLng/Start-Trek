# Start-Trek

## Project Goal

Start-Trek trains a reinforcement learning agent to land autonomously in Gymnasium `LunarLander-v3`.
The objective is to reach stable performance with a mean score of at least `200` over `100` consecutive episodes while preserving reproducibility and clear experiment traceability.

## Scope

- Language: Python
- Main libraries: Gymnasium, PyTorch
- Environment: `LunarLander-v3` (discrete first, optional continuous extension)
- Focus: RL loop fundamentals, exploration/exploitation, value-based learning before deep optimization complexity

## Project Status

Current phase: `Setup and instrumentation`.

Update this section at each milestone:
- Baseline and logging complete
- First trainable agent complete
- Ablation complete
- Reproducibility validation complete
- Final report complete

## Repository Structure

```text
Start-Trek/
  README.md
  train.py
  eval.py
  configs/
  artifacts/
  Documentations/
    PROJECT-RECAP.md
    README-INDEX.md
    report/
      REPORT-TEMPLATE.md
    changes/
      VARIABLE_REGISRTY.md
      CHANGELOG-EXPERIMENTS.md