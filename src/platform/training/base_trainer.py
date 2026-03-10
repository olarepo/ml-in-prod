from typing import List, Dict, Type
from collections import Counter
import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

from src.platform.common.validation import validate_records

from src.platform.model_registry.registry import ModelRegistry

from src.platform.experiments.experiment_tracker import ExperimentTracker

from src.platform.common.logging_config import get_logger

logger = get_logger(__name__)

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
        self.model_name = model_output_path

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

        tracker = ExperimentTracker()
        
        tracker.log_experiment(
            model_name=self.model_name,
            params=model.get_params(),
            metrics=metrics
        )

        registry = ModelRegistry()
        registry.register_model(self.model_output_path, model)

        self._log_metrics(metrics)

        return metrics

    def _log_metrics(self, metrics: Dict[str, float]):
        logger.info("Training completed")
        for k, v in metrics.items():
            logger.info(f"{k}: {v:.4f}")
        logger.info(f"Model saved to {self.model_output_path}")