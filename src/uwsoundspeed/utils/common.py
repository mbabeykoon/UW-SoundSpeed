import os
import yaml
from box.exceptions import BoxValueError 
from box import ConfigBox
from pathlib import Path
from typing import Any
import json
import joblib
from ensure import ensure_annotations
from uwsoundspeed import logger  # Ensure this logger is properly configured for your deployment
from uwsoundspeed.entity.config_entity import (DataIngestionConfig,PreprocessingConfig)
# from uwsoundspeed.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig,PreprocessingConfig,PCAConfig,ModelConfig,GridSearchConfig,TrainTestSplitConfig)
import pickle


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns ConfigBox type."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Failed to read YAML file: {path_to_yaml}, Error: {e}")
        raise e

@ensure_annotations
def create_directories(paths: list, verbose=True):
    """Creates directories from a list of paths."""
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data to a JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file and returns ConfigBox."""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib."""
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the file in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

# Customize below functions as per your project's requirements for loading/saving models

@ensure_annotations
def save_to_pkl(data: Any, path: Path):
    """Saves a Python object to a pickle file."""
    joblib.dump(data, path)
    logger.info(f"Pickle file saved to: {path}")

@ensure_annotations
def load_from_pkl(path: Path) -> Any:
    """Loads a Python object from a pickle file."""
    data = joblib.load(path)
    logger.info(f"Pickle file loaded from: {path}")
    return data
