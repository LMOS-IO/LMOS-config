import aiohttp
import asyncio
import json
from ruamel.yaml import YAML
from lmos_config.ConfigTypes import LMOSBaseConfigModel

async def _get_asset(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            file_str = await response.text()
            return file_str
        
def _load_raw_config(url, asset_str):
    if url.endswith('.json'):
        raw_config = json.loads(asset_str)
    elif url.endswith('.yaml') or url.endswith('.yml'):
        yaml = YAML(typ='safe')
        raw_config = yaml.load(asset_str)
    else:
        raise ValueError(f'Unsupported config file type found at: {url}')
    return raw_config

def load_http_config(url):
    """
    Loads the config from a http endpoints. Can be either json or yaml/yml
    
    :param url: The url to load the config from
    :return: The config as a LMOSBaseConfigModel object
    """
    file_str = asyncio.run(_get_asset(url))
    raw_config = _load_raw_config(url, file_str)
    try:
        return LMOSBaseConfigModel(**raw_config)
    except Exception as e:
        raise ValueError(f"Error validating configuration data from {url}: {e}")