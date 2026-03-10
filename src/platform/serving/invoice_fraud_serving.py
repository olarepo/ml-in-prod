from src.platform.serving.base_server import BaseServer
from src.platform.common.fraud_schema import InvoiceFraudRecord
from src.platform.features.invoice_fraud_features import build_invoice_fraud_features

class FraudServer:

    def __init__(self):

        self.server = BaseServer(
            schema_class=InvoiceFraudRecord,
            feature_builder=build_invoice_fraud_features,
            model_path="invoice_fraud_model",
            id_field="invoice_id",
            probability_field="fraud_probability",
        )

    def predict(self, records):

        return self.server.predict(records)

server = FraudServer()

def predict_invoice_fraud(records):
    return server.predict(records)