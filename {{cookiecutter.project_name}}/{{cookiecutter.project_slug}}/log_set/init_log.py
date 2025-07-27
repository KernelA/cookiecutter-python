import os
from typing import Optional
import logging.config
from importlib import resources, util
import yaml


def init_logging(log_config: Optional[str] = None, log_env_var: str = "LOG_CONFIG"):
    path_to_config = log_config or os.environ.get(log_env_var)

    if path_to_config is None:
        module_spec = util.find_spec(__name__)
        file = resources.open_binary(module_spec.parent, "log_settings.yaml")
    else:
        file = open(path_to_config, "rb")

    try:
        log_config = yaml.safe_load(file)
    finally:
        file.close()

    logging.config.dictConfig(log_config)
