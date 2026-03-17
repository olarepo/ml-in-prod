from src.platform.serving.base_server import BaseServer
from src.platform.common.churn_schema import ChurnRecord
from src.platform.features.churn_features import build_churn_features


MODEL_NAME = "churn_model"


def predict_churn(records, version=None):

    server = BaseServer(
        schema_class=ChurnRecord,
        feature_builder=build_churn_features,
        model_path=MODEL_NAME,
        id_field="customer_id",
        probability_field="churn_probability",
        version=version,
    )

    return server.predict(records)