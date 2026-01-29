from pathlib import Path
import yaml
from typing import Any, Dict


class ConfigLoader:
    """
    Centralized configuration loader.

    Loads YAML config files and exposes them as dictionaries.
    """

    def __init__(self, config_dir: str = "configs"):
        self.config_dir = Path(config_dir)

    def load(self, filename: str) -> Dict[str, Any]:
        config_path = self.config_dir / filename

        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, "r") as f:
            return yaml.safe_load(f)
