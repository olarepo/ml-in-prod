import json
from pathlib import Path

from src.platform.model_registry.registry import ModelRegistry
import joblib

ARTIFACT_DIR = Path("artifacts")

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


def promote_best_model(model_name, metric="accuracy"):

    best = best_experiment_for_model(model_name, metric)

    if not best:
        return None

    model_path = ARTIFACT_DIR / f"{model_name}.joblib"

    if not model_path.exists():
        raise ValueError(f"Model artifact not found: {model_path}")

    model = joblib.load(model_path)

    registry = ModelRegistry()
    metadata = registry.register_model(model_name, model)

    return {
        "experiment": best,
        "registry_entry": metadata
    }