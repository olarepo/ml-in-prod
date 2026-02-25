import argparse
import json
import sys

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

    parser.add_argument("action", choices=["train", "serve"])
    parser.add_argument("model", choices=MODEL_TRAINERS.keys())
    parser.add_argument("input_file", help="Path to JSON input file")

    args = parser.parse_args()

    if args.action == "train":
        trainer = MODEL_TRAINERS[args.model]
        data = load_json_file(args.input_file)
        trainer(data)

    elif args.action == "serve":
        server = MODEL_SERVERS[args.model]
        data = load_json_file(args.input_file)
        results = server(data)
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()