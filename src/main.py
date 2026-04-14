import argparse
import textwrap

parser = argparse.ArgumentParser(
    prog='Start trek',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
            Start trak is a reinforcement learning project
            that enables modules to correct its own trajectory
            to land safely on the moon"
        '''))

subparsers = parser.add_subparsers(dest="command", required=True)

#train
train_parser = subparsers.add_parser(
    "train",
    help="Run the training loop (data collection + optimization) and save metrics/checkpoints for the configured run",
)
train_parser.add_argument(
    "--config",
    type=str,
    required=True,
    help="Path to YAML config file",
)
train_parser.add_argument(
    "--run_id",
    type=str,
    help="Experiment run Id (output folder name)",
)

#eval

eval_parser = subparsers.add_parser(
    "eval",
    help="Evaluate a trained agent and export metrics",
)
eval_parser.add_argument("--config", type=str, required=True)
eval_parser.add_argument("--run_id", type=str)

#reproduce
repro_parser = subparsers.add_parser(
    "reproduce",
    help="Re-run experiements to regenerate outputs",
)
repro_parser.add_argument("--config", type=str, required=True)
repro_parser.add_argument("--run_id", type=str)

args = parser.parse_args()

print(args.config)