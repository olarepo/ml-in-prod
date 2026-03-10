import argparse
import json

from src.platform.training.late_payment_training import train_late_payment_model
from src.platform.training.invoice_fraud_training import train_invoice_fraud_model
from src.platform.training.churn_training import train_churn_model

from src.platform.serving.late_payment_serving import predict_late_payment
from src.platform.serving.invoice_fraud_serving import predict_invoice_fraud
from src.platform.serving.churn_serving import predict_churn


MODEL_TRAINERS = {
    "late_payment": train_late_payment_model,
    "invoice_fraud": train_invoice_fraud_model,
    "churn": train_churn_model,
}

MODEL_SERVERS = {
    "late_payment": predict_late_payment,
    "invoice_fraud": predict_invoice_fraud,
    "churn": predict_churn,
}


def load_json_file(path):
    with open(path, "r") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Risk ML Platform CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Train
    train_parser = subparsers.add_parser("train")
    train_parser.add_argument("model", choices=MODEL_TRAINERS.keys())
    train_parser.add_argument("input_file", help="Path to JSON input file")

    # Serve
    serve_parser = subparsers.add_parser("serve")
    serve_parser.add_argument("model", choices=MODEL_SERVERS.keys())
    serve_parser.add_argument("input_file", help="Path to JSON input file")

    # Experiments
    exp_parser = subparsers.add_parser("experiments")
    exp_parser.add_argument("subcommand", choices=["list", "best"])
    exp_parser.add_argument("--model", help="Model name")
    exp_parser.add_argument("--metric", default="accuracy", help="Metric for best experiment")

    args = parser.parse_args()

    if args.command == "train":
        trainer = MODEL_TRAINERS[args.model]
        data = load_json_file(args.input_file)
        trainer(data)

    elif args.command == "serve":
        server = MODEL_SERVERS[args.model]
        data = load_json_file(args.input_file)
        results = server(data)
        print(json.dumps(results, indent=2))

    elif args.command == "experiments":
        # Local import to avoid circular import
        from src.platform.cli import experiments as exp_cli
        import sys

        sys.argv = ["experiments.py", args.subcommand]
        if args.model:
            sys.argv += ["--model", args.model]
        if args.metric:
            sys.argv += ["--metric", args.metric]

        exp_cli.main()


if __name__ == "__main__":
    main()