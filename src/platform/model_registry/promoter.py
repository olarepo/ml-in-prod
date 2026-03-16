import json
from pathlib import Path

from src.platform.model_registry.registry import ModelRegistry


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


import joblib
from pathlib import Path

from src.platform.model_registry.registry import ModelRegistry
from src.platform.model_registry.promoter import best_experiment_for_model


def promote_best_model(model_name, metric="accuracy"):

    best = best_experiment_for_model(model_name, metric)

    if not best:
        return None

    registry = ModelRegistry()

    # Load latest trained model artifact
    model_path = Path("models") / f"{model_name}.joblib"

    if not model_path.exists():
        raise FileNotFoundError(
            f"Expected trained model artifact at {model_path}"
        )

    model = joblib.load(model_path)

    metadata = registry.register_model(
        model_name=model_name,
        model=model
    )

    return {
        "experiment_id": best["experiment_id"],
        "version": metadata["version"],
        "metric": best["metrics"].get(metric),
    }