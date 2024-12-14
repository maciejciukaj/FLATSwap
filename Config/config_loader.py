import json
import os

import whisper


def load_config():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, "config.json")

        with open(config_path, "r") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError("config.json file can't be found")
    except json.JSONDecodeError:
        raise ValueError("config.json file contains errors and cannot be loaded")

def load_model():
    config = load_config()
    model = whisper.load_model(config["model_size"], device=config["device"])
    return model