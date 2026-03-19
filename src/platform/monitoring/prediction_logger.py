import json
from pathlib import Path
from datetime import datetime


LOG_DIR = Path("prediction_logs")
LOG_DIR.mkdir(exist_ok=True)


def log_predictions(model_name, version, inputs, outputs):
    log_file = LOG_DIR / f"{model_name}.json"

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "model": model_name,
        "version": version,
        "inputs": inputs,
        "outputs": outputs,
    }

    if log_file.exists():
        with open(log_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(record)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=2)