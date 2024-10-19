import asyncio
from lmos_config._pre_config import PreConfigOptions
from lmos_config.ConfigLoader.http_config import load_http_config
from lmos_config.ConfigLoader.local_config import load_local_yaml_config
from lmos_config.ConfigTypes import LMOSBaseConfigModel

__all__ = [
    "config",
]


class LMOSConfigManagerSingleton(LMOSBaseConfigModel):
    # def __init__(self) :
    #     pass

    async def load_config_data(self) :
        try:
            if PreConfigOptions.http_url:
                config = await load_http_config(PreConfigOptions.http_url)
            elif PreConfigOptions.s3_bucket:
                # TODO implement S3 loading of config
                raise NotImplementedError("S3 config loading is not implemented yet")
            else:
                config = await load_local_yaml_config(PreConfigOptions.yaml_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load configuration: {e}. ")

        assert isinstance(config, LMOSBaseConfigModel), "Config is not of type LMOSBaseConfigModel"
        
        for field in config.model_fields:
            setattr(self, field, getattr(config, field))

config = LMOSConfigManagerSingleton.model_construct()

if PreConfigOptions.PRELOAD_CONFIG:
    asyncio.run(config.load())