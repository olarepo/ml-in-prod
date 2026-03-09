import json
from pathlib import Path

REGISTRY_METADATA_PATH = Path("models/registry.json")


def load_registry():

    if not REGISTRY_METADATA_PATH.exists():
        return {}

    with open(REGISTRY_METADATA_PATH, "r") as f:
        return json.load(f)


def save_registry(registry):

    REGISTRY_METADATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(REGISTRY_METADATA_PATH, "w") as f:
        json.dump(registry, f, indent=2)