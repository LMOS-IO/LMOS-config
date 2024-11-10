from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

from .internal_services import InternalConfiguration
from .router import RouterConfig
from .auth import AuthConfig
from .llm_runner import LLM_RUNNERS
from .tts_runner import TTS_RUNNERS
from .stt_runner import STT_RUNNERS
from .rerank_runner import RERANK_RUNNERS

class Services(BaseModel):
    """
    Configuration for all services.
    """

    router: RouterConfig = Field(
        default_factory=lambda: RouterConfig(),
        description="Configuration for the LMOS Router",
    )
    llm_runner: Optional[List[LLM_RUNNERS]] = Field(
        default_factory=list, description="List of LLM runner services"
    )
    stt_runner: Optional[List[STT_RUNNERS]] = Field(
        default_factory=list, description="List of STT runner services"
    )
    tts_runner: Optional[List[TTS_RUNNERS]] = Field(
        default_factory=list, description="List of TTS runner services"
    )
    rerank_runner: Optional[List[RERANK_RUNNERS]] = Field(
        default_factory=list, description="List of re-ranker services"
    )


# Define the main configuration model
class LMOSBaseConfigModel(BaseModel):
    """
    The global config for the entire LMOS system.

    This file is mapped provided to all containers on boot,
    and is used to configure all aspects of the system.

    The Router config is automatically derived from the services config.
    """

    internal_configuration: InternalConfiguration = Field(
        ..., description="Internal configuration for assets"
    )
    auth: AuthConfig = Field(
        default_factory=lambda: AuthConfig()
    )
    services: Services = Field(
        ..., description="Service configurations"
    )
    model_config = ConfigDict(
        title="Global LMOS Config",
    )
