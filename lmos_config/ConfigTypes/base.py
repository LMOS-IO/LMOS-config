from typing import List, Optional
from pydantic import BaseModel, AnyUrl, ConfigDict, Field

# Define the model for the internal configuration assets
class RedisConfig(BaseModel):
    """
    Redis Configuration. This tells LMOS how to connect to your redis instance.
    """
    redis_url: AnyUrl = Field(..., description="Redis Connection URL. This Should start with `redis://`")

class PrometheusConfig(BaseModel):
    """
    Configuration for Prometheus logging.
    """
    logging_enabled: bool = Field(False, description="Flag to enable or disable Prometheus logging")
    log_level: str = Field('info', description="Logging level for Prometheus, e.g., 'info', 'debug', 'error'")
    endpoint: Optional[AnyUrl] = Field(None, description="Optional endpoint URL for Prometheus logging")

class RelationalDatabaseConfig(BaseModel):
    """
    Database Configuration. This tells LMOS how to connect to your relationdatabase.
    [Engine Configuration](https://docs.sqlalchemy.org/en/20/core/engines.html)
    """
    database_url: AnyUrl = Field(..., description="Database Connection URL. This should be any sqlalchemy support url or similar")

class InternalConfiguration(BaseModel):
    """
    Config for services LMOS depends on.
    """
    redis: RedisConfig = Field(..., description="Redis Connection Configuration")
    prometheus: Optional[PrometheusConfig] = Field(None, description="Optional Prometheus Logging Configuration")
    database: RelationalDatabaseConfig = Field(..., description="Database Connection Configuration")

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
    api_key: Optional[str] = Field(None, description="Optional API key for the service")

class RouterConfig(BaseModel):
    """
    Configuration for the LMOS Router which delgates requests to the approitate service.

    `log_request_dump_volume_thresh` and `log_request_dump_time_thresh` are used to determine when to insert usage logs into the RDB.
    LMOS Router will queue usage logs internally to prevent delays in the request response cycle.

    It is recommended that you set the `log_request_dump_volume_thresh` such that it frequently triggers prior to reaching the the time limit specified by `log_request_dump_time_thresh`.
    """
    log_request_dump_volume_thresh: int = Field(1000, description="In number of entries: Threshold for worker to insert usage logs into RDB")
    log_request_dump_time_thresh: int = Field(1000, description="In Seconds: Threshold for max time between worker inserting into RDB")

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
    router: RouterConfig = Field(..., description="Configuration for the LMOS Router")
    llm_runner: Optional[List[LLMRunnerConfig]] = Field(..., description="List of LLM runner services")
    stt_runner: Optional[List[STTRunnerConfig]] = Field(..., description="List of STT runner services")
    tts_runner: Optional[List[TTSRunnerConfig]] = Field(..., description="List of TTS runner services")
    rerank_runner: Optional[List[ReRankRunnerConfig]] = Field(..., description="List of reranking services")

# Define the main configuration model
class LMOSBaseConfigModel(BaseModel):
    """
    The global config for the entire LMOS system. 
    
    This file is mapped provided to all containers on boot,
    and is used to configure all aspects of the system.

    The InferRoute config is automatically derived from the services config.
    """
    internal_configuration: InternalConfiguration = Field(..., description="Internal configuration for assets")
    services: Services = Field(..., description="Service configurations")

    model_config = ConfigDict(
        title="Global LMOS Config",
    )