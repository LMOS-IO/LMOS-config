from .ConfigTypes import LMOSBaseConfigModel

from _pre_config import PreConfigOptions

__all__ = [
    "config",
]


class ConfigManager:
    _config: LMOSBaseConfigModel

    def __init__(self):
        pass
        # self._config = LMOSBaseConfigModel()  # Initialize the config here if needed

    @property
    def config(self):
        return self._config


# Instantiate the config manager
config = ConfigManager()
