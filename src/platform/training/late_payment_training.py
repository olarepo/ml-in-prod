from typing import List
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

from src.platform.common.schema import LatePaymentRecord
from src.platform.common.validation import validate_records
from src.platform.features.late_payment_features import build_late_payment_features


MODEL_OUTPUT_PATH = "models/late_payment_model.joblib"


def train_late_payment_model(records: List[dict]) -> None:
    """
    End-to-end training pipeline:
    - Validate input
    - Build features
    - Train logistic regression
    - Persist model
    """

    # 1️⃣ Validate records
    validated = validate_records(records, LatePaymentRecord)

    # 2️⃣ Build features
    feature_dicts = [build_late_payment_features(r) for r in validated]

    X = np.array([list(f.values()) for f in feature_dicts])
    y = np.array([r.label for r in validated])

    # 3️⃣ Train model
    model = LogisticRegression()
    model.fit(X, y)

    # 4️⃣ Persist model
    joblib.dump(model, MODEL_OUTPUT_PATH)

    print(f"Model saved to {MODEL_OUTPUT_PATH}")