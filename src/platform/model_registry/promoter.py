import json
from pathlib import Path


EXPERIMENT_FILE = Path("experiments/experiments.json")


def load_experiments():
    if not EXPERIMENT_FILE.exists():
        return []

    with open(EXPERIMENT_FILE, "r") as f:
        return json.load(f)


def best_experiment_for_model(model_name, metric="accuracy"):
    experiments = load_experiments()

    model_experiments = [
        e for e in experiments if e["model"] == model_name
    ]

    if not model_experiments:
        return None

    best = max(
        model_experiments,
        key=lambda e: e["metrics"].get(metric, 0)
    )

    return best