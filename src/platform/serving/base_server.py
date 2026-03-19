from typing import List, Dict, Type
import numpy as np
import joblib

from src.platform.model_registry.registry import ModelRegistry

from src.platform.common.validation import validate_records

from src.platform.common.logging_config import get_logger
from src.platform.monitoring.prediction_logger import log_predictions

logger = get_logger(__name__)

class BaseServer:
    """
    Abstract serving template for classification models.
    """

    def __init__(
        self,
        schema_class: Type,
        feature_builder,
        model_path: str,
        id_field: str,
        probability_field: str,
        version=None,
    ):
        self.schema_class = schema_class
        self.feature_builder = feature_builder
        self.model_path = model_path
        self.id_field = id_field
        self.probability_field = probability_field
        self.version = version

    def _load_model(self):
        registry = ModelRegistry()

        if self.version is not None:
            return registry.load_model_version(self.model_path, self.version)

        return registry.load_latest_model(self.model_path)
        

    def predict(self, records: List[dict]) -> List[Dict]:
        logger.info(f"Received {len(records)} records for prediction")

        validated = validate_records(records, self.schema_class)

        feature_dicts = [self.feature_builder(r) for r in validated]
        X = np.array([list(f.values()) for f in feature_dicts])

        model = self._load_model()

        probabilities = model.predict_proba(X)[:, 1]
        predictions = model.predict(X)

        logger.info("Prediction completed")

        results = []

        for record, prob, pred in zip(validated, probabilities, predictions):
            results.append({
                self.id_field: getattr(record, self.id_field),
                self.probability_field: float(prob),
                "predicted_label": int(pred),
            })

        # Log predictions
        log_predictions(
            model_name=self.model_path,
            version=self.version or "latest",
            inputs=records,
            outputs=results
        )
        return results