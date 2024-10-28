"""This module provides a globally defined mechanism for a runner component
to determine what model instance config it is supposed to load"""

from pydantic import Field
from pydantic_settings import BaseSettings


class RunnerInstanceSettings(BaseSettings):
    type: str = Field(description="the name of the model to run")

    class Config:
        env_prefix = "LMOS_RUNNER_"


InstanceConfig = RunnerInstanceSettings()
