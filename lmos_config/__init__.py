import os
import yaml
from .ConfigTypes import LMOSBaseConfigModel

from _pre_config import PreConfigOptions

__all__ = [
    "config",
]

DEFAULT_CONFIG_PATH = '/usr/src/app/config.yaml'

def get_config_file_path():
    # First, check for CONFIG_PATH environment variable
    config_path = os.environ.get('CONFIG_PATH')
    
    if config_path:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at path specified by CONFIG_PATH: {config_path}")
        return config_path
    
    # If CONFIG_PATH is not set, use the default path
    if not os.path.exists(DEFAULT_CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found at default path: {DEFAULT_CONFIG_PATH}. "
                                f"Please set the CONFIG_PATH environment variable to specify a custom location, "
                                f"or ensure the config file exists at the default location: {DEFAULT_CONFIG_PATH}")

    return DEFAULT_CONFIG_PATH

# Function to load and parse the YAML configuration file
def load_config():
    config_file_path = get_config_file_path()

    try:
        # Open and read the YAML config file
        with open(config_file_path, "r") as file:
            config_data = yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML configuration file at {config_file_path}: {e}")

    try:
        # Validate and parse the config using LMOSBaseConfigModel
        return LMOSBaseConfigModel(**config_data)
    except Exception as e:
        raise ValueError(f"Error validating configuration data from {config_file_path}: {e}")

# Load the configuration at the time of importl
try:
    config = load_config()
except Exception as e:
    raise RuntimeError(f"Failed to load configuration: {e}. "
                       f"Ensure the config file exists at {DEFAULT_CONFIG_PATH} "
                       f"or set the CONFIG_PATH environment variable.")
