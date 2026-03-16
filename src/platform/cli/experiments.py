import json
from pathlib import Path
import argparse

from src.platform.model_registry.promoter import best_experiment_for_model


EXPERIMENT_FILE = Path("experiments/experiments.json")


def load_experiments():
    if not EXPERIMENT_FILE.exists():
        return []
    with open(EXPERIMENT_FILE, "r") as f:
        return json.load(f)


def list_experiments(model_name=None):
    experiments = load_experiments()
    if model_name:
        experiments = [e for e in experiments if e["model"] == model_name]

    for e in experiments:
        print(
            f"ID: {e['experiment_id']}, Model: {e['model']}, "
            f"Metrics: {e['metrics']}, Timestamp: {e['timestamp']}"
        )


def best_experiment(model_name, metric="accuracy"):
    experiments = load_experiments()
    model_exps = [e for e in experiments if e["model"] == model_name]
    if not model_exps:
        print(f"No experiments found for model '{model_name}'")
        return
    best = max(model_exps, key=lambda e: e["metrics"].get(metric, 0))
    print(
        f"Best Experiment ID: {best['experiment_id']}, Model: {best['model']}, "
        f"{metric}: {best['metrics'].get(metric)}, Timestamp: {best['timestamp']}"
    )

def promote_model(model_name, metric="accuracy"):

    best = best_experiment_for_model(model_name, metric)

    if not best:
        print(f"No experiments found for model '{model_name}'")
        return

    print(
        f"Promoting experiment {best['experiment_id']} "
        f"with {metric}={best['metrics'].get(metric)}"
    )

    print("Model promotion simulated (registry integration next)")

def main():
    parser = argparse.ArgumentParser(description="Experiment CLI")
    parser.add_argument("command", choices=["list", "best", "promote"])
    parser.add_argument("--model", help="Model name")
    parser.add_argument("--metric", default="accuracy", help="Metric for best")
    args = parser.parse_args()

    if args.command == "list":
        list_experiments(args.model)
    elif args.command == "best":
        if not args.model:
            print("Please provide --model for best command")
        else:
            best_experiment(args.model, args.metric)
    elif args.command == "promote":
        if not args.model:
            print("Please provide --model for promote command")
        else:
            promote_model(args.model, args.metric)

