from typing import List, Dict
import joblib
import numpy as np

from src.platform.common.validation import validate_records
from src.platform.common.fraud_schema import InvoiceFraudRecord
from src.platform.features.invoice_fraud_features import build_invoice_fraud_features


MODEL_PATH = "models/invoice_fraud_model.joblib"


def load_model(path: str = MODEL_PATH):
    return joblib.load(path)


def predict_invoice_fraud(records: List[dict]) -> List[Dict]:

    validated = validate_records(records, InvoiceFraudRecord)

    feature_dicts = [build_invoice_fraud_features(r) for r in validated]
    X = np.array([list(f.values()) for f in feature_dicts])

    model = load_model()

    probabilities = model.predict_proba(X)[:, 1]
    predictions = model.predict(X)

    results = []

    for record, prob, pred in zip(validated, probabilities, predictions):
        results.append({
            "invoice_id": record.invoice_id,
            "fraud_probability": float(prob),
            "predicted_label": int(pred),
        })

    return results