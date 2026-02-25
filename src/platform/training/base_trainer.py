# src/platform/training/base_trainer.py

from typing import List, Dict, Type
from collections import Counter
import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

from src.platform.common.validation import validate_records


class BaseTrainer:
    """
    Abstract training template for classification models.
    """

    RANDOM_STATE = 42
    TEST_SIZE = 0.3

    def __init__(self, schema_class: Type, feature_builder, model_output_path: str):
        self.schema_class = schema_class
        self.feature_builder = feature_builder
        self.model_output_path = model_output_path

    def _validate_dataset(self, y: np.ndarray):
        class_counts = Counter(y)

        if len(class_counts) < 2:
            raise ValueError("Training requires at least two classes.")

        if min(class_counts.values()) < 2:
            raise ValueError(
                f"Each class must have at least 2 samples. Got: {class_counts}"
            )

    def train(self, records: List[dict]) -> Dict[str, float]:

        validated = validate_records(records, self.schema_class)

        feature_dicts = [self.feature_builder(r) for r in validated]

        X = np.array([list(f.values()) for f in feature_dicts])
        y = np.array([r.label for r in validated])

        self._validate_dataset(y)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.TEST_SIZE,
            random_state=self.RANDOM_STATE,
            stratify=y,
        )

        model = LogisticRegression(random_state=self.RANDOM_STATE)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        metrics = {
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions, zero_division=0),
            "recall": recall_score(y_test, predictions, zero_division=0),
        }

        joblib.dump(model, self.model_output_path)

        self._print_metrics(metrics)

        return metrics

    def _print_metrics(self, metrics: Dict[str, float]):
        print("Model Metrics:")
        for k, v in metrics.items():
            print(f"{k}: {v:.4f}")
        print(f"\nModel saved to {self.model_output_path}")