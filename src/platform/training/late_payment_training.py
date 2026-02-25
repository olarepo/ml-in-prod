from src.platform.training.base_trainer import BaseTrainer
from src.platform.common.schema import LatePaymentRecord
from src.platform.features.late_payment_features import build_late_payment_features


MODEL_OUTPUT_PATH = "models/late_payment_model.joblib"


def train_late_payment_model(records):
    trainer = BaseTrainer(
        schema_class=LatePaymentRecord,
        feature_builder=build_late_payment_features,
        model_output_path=MODEL_OUTPUT_PATH,
    )

    return trainer.train(records)