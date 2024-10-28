from ruamel.yaml import YAML
from lmos_config.ConfigTypes import LMOSBaseConfigModel


# Function to load and parse the YAML configuration file
async def load_local_yaml_config(config_file_path):
    """
    Loads the yaml from the local file system

    :param config_file_path: Path to the YAML configuration file
    :return: The config as a LMOSBaseConfigModel object
    """
    try:
        # Open and read the YAML config file

        with open(config_file_path, "r") as file:
            config_data = YAML(typ="safe").load(file)
    except Exception as e:
        raise ValueError(
            f"Error parsing YAML configuration file at {config_file_path}: {e}"
        )

    try:
        # Validate and parse the config using LMOSBaseConfigModel
        return LMOSBaseConfigModel(**config_data)
    except Exception as e:
        raise ValueError(
            f"Error validating configuration data from {config_file_path}: {e}"
        )
