# Start-Trek

## Project Goal

Start-Trek trains a reinforcement learning agent to land autonomously in Gymnasium `LunarLander-v3`.
The objective is to reach stable performance with a mean score of at least `200` over `100` consecutive episodes while preserving reproducibility and clear experiment traceability.

## Scope

- Language: Python
- Main libraries: Gymnasium, PyTorch
- Environment: `LunarLander-v3` (discrete first, optional continuous extension)
- Focus: RL loop fundamentals, exploration/exploitation, value-based learning before deep optimization complexity

## Quick start (CLI)

From the repository root, with dependencies installed (including PyYAML):

```bash
python -m src.main train --config configs/baseline.yaml
python -m src.main train --config configs/baseline.yaml --run-id my-run-001
python -m src.main eval --config configs/baseline.yaml
python -m src.main reproduce --config configs/baseline.yaml
```

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
  src/
    main.py
    training/
      train.py
      metrics.py
  configs/
    baseline.yaml
  scripts/
    reproduce.sh
  artifacts/
  Documentations/
    PROJECT-RECAP.md
    README-INDEX.md
    report/
      REPORT-TEMPLATE.md
    changes/
      VARIABLE-REGISTRY.md
      CHANGELOG-EXPERIMENTS.md
      VARIABLE-EXPLAINED.md