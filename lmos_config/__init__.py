from _pre_config import PreConfigOptions
from lmos_config.ConfigLoader.local_config import load_local_yaml_config
from lmos_config.ConfigLoader.http_config import load_http_config
from lmos_config.ConfigTypes import LMOSBaseConfigModel

__all__ = [
    "config",
]

config: LMOSBaseConfigModel

try:
    if PreConfigOptions.http_url:
        config = load_http_config(PreConfigOptions.http_url)
    elif PreConfigOptions.s3_bucket:
        raise NotImplementedError("S3 config loading is not implemented yet")
    else:
        config = load_local_yaml_config(PreConfigOptions.yaml_path)
except Exception as e:
    raise RuntimeError(f"Failed to load configuration: {e}. ")

assert isinstance(config, LMOSBaseConfigModel), "Config is not of type LMOSBaseConfigModel"