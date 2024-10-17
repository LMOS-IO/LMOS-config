from typing import List, Optional
from pydantic import BaseModel, AnyUrl, Field

# Define the model for the internal configuration assets
class RedisConfig(BaseModel):
    """
    Configuration for Redis asset.
    """
    redis_url: AnyUrl = Field(..., description="URL for Redis configuration")

class PrometheusConfig(BaseModel):
    """
    Configuration for Prometheus logging.
    """
    logging_enabled: bool = Field(..., description="Flag to enable or disable Prometheus logging")
    log_level: str = Field(..., description="Logging level for Prometheus, e.g., 'info', 'debug', 'error'")
    endpoint: Optional[AnyUrl] = Field(None, description="Optional endpoint URL for Prometheus logging")

class InternalConfiguration(BaseModel):
    """
    Internal configuration for various assets.
    """
    redis: RedisConfig = Field(..., description="Redis configuration")
    prometheus: Optional[PrometheusConfig] = Field(None, description="Prometheus configuration, optional")  # Prometheus config can be added later

# Define the generic model for services
class GenericServiceConfig(BaseModel):
    """
    Generic configuration for services.
    """
    name: str = Field(..., description="Name of the service")
    location: str = Field(..., description="Path to the model folder or HF repository")
    alias: List[str] = Field(default_factory=list, description="List of aliases for the service")
    type: Optional[str] = Field(None, description="Type of backend for the service, optional")  # Some services have a "type" field
    endpoint: Optional[AnyUrl] = Field(None, description="Optional endpoint URL for the service")

# Define specific service configurations that can inherit from GenericServiceConfig
class LLMRunnerConfig(GenericServiceConfig):
    """
    Configuration for LLM runner services.
    """
    pass

class STTRunnerConfig(GenericServiceConfig):
    """
    Configuration for STT runner services.
    """
    pass

class TTSRunnerConfig(GenericServiceConfig):
    """
    Configuration for TTS runner services.
    """
    pass

class ReRankRunnerConfig(GenericServiceConfig):
    """
    Configuration for reranking services.
    """
    pass

class Services(BaseModel):
    """
    Configuration for all services.
    """
    llm_runner: List[LLMRunnerConfig] = Field(..., description="List of LLM runner services")
    stt_runner: List[STTRunnerConfig] = Field(..., description="List of STT runner services")
    tts_runner: List[TTSRunnerConfig] = Field(..., description="List of TTS runner services")
    rerank_runner: List[ReRankRunnerConfig] = Field(..., description="List of reranking services")

# Define the main configuration model
class LMOSBaseConfigModel(BaseModel):
    """
    Main configuration model that includes internal assets and services.
    """
    internal_configuration: InternalConfiguration = Field(..., description="Internal configuration for assets")
    services: Services = Field(..., description="Service configurations")