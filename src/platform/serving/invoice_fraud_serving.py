from src.platform.serving.base_server import BaseServer
from src.platform.common.fraud_schema import InvoiceFraudRecord
from src.platform.features.invoice_fraud_features import build_invoice_fraud_features


MODEL_NAME = "invoice_fraud_model"


def predict_invoice_fraud(records, version=None):

    server = BaseServer(
        schema_class=InvoiceFraudRecord,
        feature_builder=build_invoice_fraud_features,
        model_path=MODEL_NAME,
        id_field="invoice_id",
        probability_field="fraud_probability",
        version=version,
    )

    return server.predict(records)