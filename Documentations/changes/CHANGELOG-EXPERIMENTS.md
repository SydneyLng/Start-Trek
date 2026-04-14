# Experiment Changelog

This changelog records all meaningful experiment and configuration changes with justification and outcomes.

## Entry Template

## [CHANGE_ID] Title
- Date:
- Author:
- Status: proposed / validated / rejected
- Related run IDs:
- Related configs:
- Related variables:

### Context
What issue or objective motivated this change.

### Change Description
What was modified (config, logic, environment setting, logging, evaluation protocol).

### Hypothesis
What improvement or behavior change was expected.

### Validation Method
How the change was tested (seeds, episodes, metrics, comparison baseline).

### Result
What happened in practice.

### Decision
Keep / revert / iterate.

### Notes
Additional observations, caveats, next actions.

---

## [CHG-0001] Initial Baseline and Instrumentation
- Date:
- Author:
- Status: proposed
- Related run IDs:
- Related configs:
- Related variables:

### Context
Need a baseline to compare all future improvements and verify logging quality.

### Change Description
Set up random and simple heuristic baselines with metric logging and termination reason tracking.

### Hypothesis
A clear baseline will expose failure modes and improve iteration quality.

### Validation Method
Run at least 5 seeds and record return, episode length, and termination breakdown.

### Result
Pending.

### Decision
Pending.

### Notes
Pending.