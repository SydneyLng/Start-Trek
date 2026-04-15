from datetime import datetime as dt
from pathlib import Path
import shutil
import json
import yaml

def run_train(config_path: str, run_id: str | None = None) -> None:
    config_file = Path(config_path)
    with config_file.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if run_id is None:
        run_id = dt.now().strftime("%Y%m%d_%H%M%S")

    root_directory = Path(config["output"]["root_directory"])
    run_directory = root_directory / run_id
    plots_directory = run_directory / "plots"
    videos_directory = run_directory / "videos"

    run_directory.mkdir(parents=True, exist_ok=True)
    plots_directory.mkdir(parents=True, exist_ok=True)
    videos_directory.mkdir(parents=True, exist_ok=True)

    shutil.copy2(config_file, run_directory / "config.yaml")

    metrics_file = run_directory / "metrics.csv"
    metrics_file.write_text(
        "episode,return,episode_length,terminated,truncated,termination_reason\n",
        encoding="utf_8",
    )

    summary = {
        "run_id": run_id,
        "config_path": str(config_file),
        "seed": config.get("run", {}).get("seed"),
        "status": "initialized",
    }
    (run_directory / "summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding=("utf-8"),
    )

    print(f"Run is initialiazed at {run_directory}")

