import json
from datetime import datetime
from pathlib import Path


EXPERIMENT_FILE = Path("experiments/experiments.json")


class ExperimentTracker:

    def __init__(self):

        EXPERIMENT_FILE.parent.mkdir(exist_ok=True)

        if not EXPERIMENT_FILE.exists():
            with open(EXPERIMENT_FILE, "w") as f:
                json.dump([], f)

    def log_experiment(self, model_name, params, metrics):

        with open(EXPERIMENT_FILE, "r") as f:
            experiments = json.load(f)

        experiment = {
            "experiment_id": len(experiments) + 1,
            "model": model_name,
            "params": params,
            "metrics": metrics,
            "timestamp": datetime.utcnow().isoformat()
        }

        experiments.append(experiment)

        with open(EXPERIMENT_FILE, "w") as f:
            json.dump(experiments, f, indent=2)

        return experiment