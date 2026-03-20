import joblib
from pathlib import Path
from datetime import datetime

from src.platform.model_registry.metadata_store import load_registry, save_registry
from src.platform.common.logging_config import get_logger

logger = get_logger(__name__)


class ModelRegistry:

    MODEL_DIR = Path("models")

    def register_model(self, model_name, model):

        registry = load_registry()

        model_versions = registry.get(model_name, [])

        new_version = len(model_versions) + 1

        model_path = self.MODEL_DIR / f"{model_name}_v{new_version}.joblib"

        self.MODEL_DIR.mkdir(exist_ok=True)

        joblib.dump(model, model_path)

        metadata = {
            "version": new_version,
            "path": model_path.as_posix(),
            "created_at": datetime.utcnow().isoformat()
        }

        model_versions.append(metadata)

        registry[model_name] = model_versions

        save_registry(registry)

        logger.info(f"Registered model {model_name} version {new_version}")

        return metadata


    def load_latest_model(self, model_name):

        registry = load_registry()

        if model_name not in registry:
            raise ValueError(f"No models registered for {model_name}")

        latest = registry[model_name][-1]

        logger.info(f"Loading model {model_name} version {latest['version']}")

        return joblib.load(latest["path"])
    
    def load_model_version(self, model_name, version):

        registry = load_registry()

        if model_name not in registry:
            raise ValueError(f"No models registered for {model_name}")

        versions = registry[model_name]

        for v in versions:
            if v["version"] == version:

                logger.info(
                    f"Loading model {model_name} version {version}"
                )

                return joblib.load(v["path"])

        raise ValueError(
            f"Version {version} not found for model {model_name}"
        )