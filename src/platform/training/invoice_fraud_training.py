# src/platform/training/invoice_fraud_training.py

from src.platform.training.base_trainer import BaseTrainer
from src.platform.common.fraud_schema import InvoiceFraudRecord
from src.platform.features.invoice_fraud_features import build_invoice_fraud_features


MODEL_OUTPUT_PATH = "models/invoice_fraud_model.joblib"


def train_invoice_fraud_model(records):
    trainer = BaseTrainer(
        schema_class=InvoiceFraudRecord,
        feature_builder=build_invoice_fraud_features,
        model_output_path=MODEL_OUTPUT_PATH,
    )

    return trainer.train(records)