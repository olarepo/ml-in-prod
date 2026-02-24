from typing import List, Dict
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

from src.platform.common.validation import validate_records
from src.platform.common.churn_schema import ChurnRecord
from src.platform.features.churn_features import build_churn_features


MODEL_OUTPUT_PATH = "models/churn_model.joblib"
RANDOM_STATE = 42


def train_churn_model(records: List[dict]) -> Dict[str, float]:
    """
    Training pipeline for churn prediction.
    """

    validated = validate_records(records, ChurnRecord)

    feature_dicts = [build_churn_features(r) for r in validated]

    X = np.array([list(f.values()) for f in feature_dicts])
    y = np.array([r.label for r in validated])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=RANDOM_STATE,
        stratify=y if len(set(y)) > 1 else None,
    )

    model = LogisticRegression(random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
    }

    joblib.dump(model, MODEL_OUTPUT_PATH)

    print("Churn Model Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    print(f"\nModel saved to {MODEL_OUTPUT_PATH}")

    return metrics