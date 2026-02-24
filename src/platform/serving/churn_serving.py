from typing import List, Dict
import joblib
import numpy as np

from src.platform.common.validation import validate_records
from src.platform.common.churn_schema import ChurnRecord
from src.platform.features.churn_features import build_churn_features


MODEL_PATH = "models/churn_model.joblib"


def load_model(path: str = MODEL_PATH):
    return joblib.load(path)


def predict_churn(records: List[dict]) -> List[Dict]:

    validated = validate_records(records, ChurnRecord)

    feature_dicts = [build_churn_features(r) for r in validated]
    X = np.array([list(f.values()) for f in feature_dicts])

    model = load_model()

    probabilities = model.predict_proba(X)[:, 1]
    predictions = model.predict(X)

    results = []

    for record, prob, pred in zip(validated, probabilities, predictions):
        results.append({
            "customer_id": record.customer_id,
            "churn_probability": float(prob),
            "predicted_label": int(pred),
        })

    return results