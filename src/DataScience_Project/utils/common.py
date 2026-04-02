import os
import json
from box.exceptions import BoxValueError
import yaml
from src.DataScience_Project import logger
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns"""

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            logger.info(
                f"yaml file: {path_to_yaml} loaded successfully"
            )

            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(
    path_to_directories: list,
    verbose: bool = True
):
    """create list of directories"""

    for path in path_to_directories:

        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data            