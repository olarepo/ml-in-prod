from src.platform.serving.base_server import BaseServer
from src.platform.common.churn_schema import ChurnRecord
from src.platform.features.churn_features import build_churn_features


MODEL_PATH = "models/churn_model.joblib"


def predict_churn(records):
    server = BaseServer(
        schema_class=ChurnRecord,
        feature_builder=build_churn_features,
        model_path=MODEL_PATH,
        id_field="customer_id",
        probability_field="churn_probability",
    )

    return server.predict(records)