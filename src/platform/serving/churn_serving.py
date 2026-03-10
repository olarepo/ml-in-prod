from src.platform.serving.base_server import BaseServer
from src.platform.common.churn_schema import ChurnRecord
from src.platform.features.churn_features import build_churn_features


class ChurnServer:

    def __init__(self):

        self.server = BaseServer(
            schema_class=ChurnRecord,
            feature_builder=build_churn_features,
            model_path="churn_model",
            id_field="customer_id",
            probability_field="churn_probability",
        )

    def predict(self, records):

        return self.server.predict(records)
    
server = ChurnServer()

def predict_churn(records):
        return server.predict(records)