import os

os.environ["LMOS_CONFIG_YAML_PATH"] = (
    "../example_configurations/lmos-config-example.yaml"
)

import asyncio
from lmos_config import config

asyncio.run(config.load_config_data())
print(config)
