import os
os.environ['LMOS_CONFIG_HTTP_URL'] = "http://localhost:5500/example_configurations/lmos-config-example.yaml"
os.environ['LMOS_CONFIG_YAML_PATH'] = "DOESNOTWORK"

import asyncio
from lmos_config import config

asyncio.run(config.load_config_data())
print(config)