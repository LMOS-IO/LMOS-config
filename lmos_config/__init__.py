import os
from _pre_config import PreConfigOptions
from lmos_config.ConfigLoader.local_yaml import load_local_yaml_config
from lmos_config.ConfigTypes import LMOSBaseConfigModel

__all__ = [
    "config",
]

config: LMOSBaseConfigModel

try:
    if PreConfigOptions.http_url:
        # load via http
        ...
    elif PreConfigOptions.s3_bucket:
        # load via s3
        ...
    else:
        config = load_local_yaml_config(PreConfigOptions.yaml_path)
except Exception as e:
    raise RuntimeError(f"Failed to load configuration: {e}. ")

assert isinstance(config, LMOSBaseConfigModel), "Config is not of type LMOSBaseConfigModel"