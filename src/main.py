import argparse
import textwrap
from src.training.train import run_train

def handle_train(args):
    run_train(config_path=args.config, run_id=args.run_id)


def handle_eval(args):
    print(f"Evaluating config={args.config} with run_id={args.run_id}")


def handle_reproduce(args):
    print(f"Reproducing config={args.config} with run_id={args.run_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Start trek",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """\
            Start trek is a reinforcement learning project
            that enables modules to correct their own trajectory
            to land safely on the moon.
            """
        ),
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    train_parser = subparsers.add_parser(
        "train",
        help="Run training and save metrics/checkpoints for a configured run.",
    )
    train_parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to YAML config file.",
    )
    train_parser.add_argument(
        "--run-id",
        type=str,
        help="Experiment run ID (output folder name).",
    )
    train_parser.set_defaults(handler=handle_train)

    eval_parser = subparsers.add_parser(
        "eval",
        help="Evaluate a trained agent and export performance metrics.",
    )
    eval_parser.add_argument("--config", type=str, required=True, help="Path to YAML config file.")
    eval_parser.add_argument("--run-id", type=str, help="Experiment run ID (output folder name).")
    eval_parser.set_defaults(handler=handle_eval)

    reproduce_parser = subparsers.add_parser(
        "reproduce",
        help="Re-run configured experiments to regenerate outputs.",
    )
    reproduce_parser.add_argument("--config", type=str, required=True, help="Path to YAML config file.")
    reproduce_parser.add_argument("--run-id", type=str, help="Experiment run ID (output folder name).")
    reproduce_parser.set_defaults(handler=handle_reproduce)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()