from src.platform.serving.base_server import BaseServer
from src.platform.common.schema import LatePaymentRecord
from src.platform.features.late_payment_features import build_late_payment_features


MODEL_PATH = "models/late_payment_model.joblib"


def predict_late_payment(records):
    server = BaseServer(
        schema_class=LatePaymentRecord,
        feature_builder=build_late_payment_features,
        model_path=MODEL_PATH,
        id_field="customer_id",
        probability_field="risk_probability",
    )

    return server.predict(records)