from typing import List, Dict
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

from src.platform.common.schema import LatePaymentRecord
from src.platform.common.validation import validate_records
from src.platform.features.late_payment_features import build_late_payment_features


MODEL_OUTPUT_PATH = "models/late_payment_model.joblib"
RANDOM_STATE = 42  # Ensures deterministic splitting


def train_late_payment_model(records: List[dict]) -> Dict[str, float]:
    """
    End-to-end training pipeline:
    - Validate input
    - Build features
    - Deterministic train/test split
    - Train logistic regression
    - Evaluate
    - Persist model
    """

    # 1️⃣ Validate records
    validated = validate_records(records, LatePaymentRecord)

    # 2️⃣ Build features
    feature_dicts = [build_late_payment_features(r) for r in validated]

    X = np.array([list(f.values()) for f in feature_dicts])
    y = np.array([r.label for r in validated])

    # 3️⃣ Deterministic split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=RANDOM_STATE,
        stratify=y if len(set(y)) > 1 else None,
    )

    # 4️⃣ Train model
    model = LogisticRegression(random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    # 5️⃣ Evaluate
    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
    }

    print("Evaluation Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    # 6️⃣ Persist model
    joblib.dump(model, MODEL_OUTPUT_PATH)
    print(f"\nModel saved to {MODEL_OUTPUT_PATH}")

    return metrics