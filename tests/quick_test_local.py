import os
os.environ['LMOS_CONFIG_YAML_PATH'] = "../example_configurations/lmos-config-example.yaml"
from lmos_config import config

print(config)