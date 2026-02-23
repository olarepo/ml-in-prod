from typing import List, Dict
import joblib
import numpy as np

from src.platform.common.schema import LatePaymentRecord
from src.platform.common.validation import validate_records
from src.platform.features.late_payment_features import build_late_payment_features


MODEL_PATH = "models/late_payment_model.joblib"


def load_model(path: str = MODEL_PATH):
    """
    Load trained model from disk.
    """
    return joblib.load(path)


def predict_late_payment(records: List[dict]) -> List[Dict]:
    """
    Full inference pipeline:
    - Validate input
    - Build features
    - Load model
    - Generate predictions
    - Return structured output
    """

    # 1️⃣ Validate
    validated = validate_records(records, LatePaymentRecord)

    # 2️⃣ Build features
    feature_dicts = [build_late_payment_features(r) for r in validated]
    X = np.array([list(f.values()) for f in feature_dicts])

    # 3️⃣ Load model
    model = load_model()

    # 4️⃣ Predict probabilities + labels
    probabilities = model.predict_proba(X)[:, 1]
    predictions = model.predict(X)

    # 5️⃣ Structure output
    results = []

    for record, prob, pred in zip(validated, probabilities, predictions):
        results.append({
            "customer_id": record.customer_id,
            "risk_probability": float(prob),
            "predicted_label": int(pred),
        })

    return results