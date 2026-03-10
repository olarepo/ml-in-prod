from src.platform.serving.base_server import BaseServer
from src.platform.common.schema import LatePaymentRecord
from src.platform.features.late_payment_features import build_late_payment_features

class LatePaymentServer:

    def __init__(self):

        self.server = BaseServer(
            schema_class=LatePaymentRecord,
            feature_builder=build_late_payment_features,
            model_path="late_payment_model",
            id_field="customer_id",
            probability_field="risk_probability",
        )

    def predict(self, records):

        return self.server.predict(records)
    
server = LatePaymentServer()

def predict_late_payment(records):
    return server.predict(records)


