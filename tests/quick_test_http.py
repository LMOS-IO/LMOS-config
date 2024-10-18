import os
os.environ['LMOS_CONFIG_HTTP_URL'] = "http://localhost:5500/example_configurations/lmos-config-example.yaml"
os.environ['LMOS_CONFIG_YAML_PATH'] = "DOESNOTWORK"
from lmos_config import config

print(config)