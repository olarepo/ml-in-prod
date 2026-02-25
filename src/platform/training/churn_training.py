# src/platform/training/churn_training.py

from src.platform.training.base_trainer import BaseTrainer
from src.platform.common.churn_schema import ChurnRecord
from src.platform.features.churn_features import build_churn_features


MODEL_OUTPUT_PATH = "models/churn_model.joblib"


def train_churn_model(records):
    trainer = BaseTrainer(
        schema_class=ChurnRecord,
        feature_builder=build_churn_features,
        model_output_path=MODEL_OUTPUT_PATH,
    )

    return trainer.train(records)