from lmos_config.ConfigTypes import LMOSBaseConfigModel as model
import json

with open("schema.json", "w") as file:
    json.dump(obj=model.model_json_schema(), fp=file)
