from .ConfigTypes import LMOSBaseConfigModel

__all__ = [
    "config",
]


class ConfigManager:
    _config: LMOSBaseConfigModel

    def __init__(self):
        self._config = LMOSBaseConfigModel()  # Initialize the config here if needed

    @property
    def config(self):
        return self._config


# Instantiate the config manager
config = ConfigManager()
