from typing import List, Dict, Type
import numpy as np
import joblib

from src.platform.common.validation import validate_records


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
    ):
        self.schema_class = schema_class
        self.feature_builder = feature_builder
        self.model_path = model_path
        self.id_field = id_field
        self.probability_field = probability_field

    def _load_model(self):
        return joblib.load(self.model_path)

    def predict(self, records: List[dict]) -> List[Dict]:

        validated = validate_records(records, self.schema_class)

        feature_dicts = [self.feature_builder(r) for r in validated]
        X = np.array([list(f.values()) for f in feature_dicts])

        model = self._load_model()

        probabilities = model.predict_proba(X)[:, 1]
        predictions = model.predict(X)

        results = []

        for record, prob, pred in zip(validated, probabilities, predictions):
            results.append({
                self.id_field: getattr(record, self.id_field),
                self.probability_field: float(prob),
                "predicted_label": int(pred),
            })

        return results