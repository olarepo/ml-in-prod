# src/platform/training/churn_training.py

from src.platform.training.base_trainer import BaseTrainer
from src.platform.common.churn_schema import ChurnRecord
from src.platform.features.churn_features import build_churn_features


MODEL_NAME = "churn_model"


def train_churn_model(records):
    trainer = BaseTrainer(
        schema_class=ChurnRecord,
        feature_builder=build_churn_features,
        model_output_path=MODEL_NAME,
    )

    return trainer.train(records)