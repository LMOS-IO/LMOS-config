from typing import List, Optional
from pydantic import BaseModel, AnyUrl, ConfigDict, Field

from .llm_runner import LLM_RUNNERS
from .tts_runner import TTS_RUNNERS
from .stt_runner import STT_RUNNERS
from .rerank_runner import RERANK_RUNNERS


# Define the model for the internal configuration assets
class RedisConfig(BaseModel):
    """
    Redis Configuration. This tells LMOS how to connect to your redis instance.
    """

    redis_url: AnyUrl = Field(
        ..., description="Redis Connection URL. This Should start with `redis://`"
    )


class PrometheusConfig(BaseModel):
    """
    Configuration for Prometheus logging.
    """

    logging_enabled: bool = Field(
        False, description="Flag to enable or disable Prometheus logging"
    )
    log_level: str = Field(
        "info",
        description="Logging level for Prometheus, e.g., 'info', 'debug', 'error'",
    )
    endpoint: Optional[AnyUrl] = Field(
        None, description="Optional endpoint URL for Prometheus logging"
    )


class RelationalDatabaseConfig(BaseModel):
    """
    Database Configuration. This tells LMOS how to connect to your relational database.
    [Engine Configuration](https://docs.sqlalchemy.org/en/20/core/engines.html)
    """

    database_url: AnyUrl = Field(
        ...,
        description="Database Connection URL. This should be any SQLAlchemy support url or similar",
    )


class InternalConfiguration(BaseModel):
    """
    Config for services LMOS depends on.
    """

    redis: RedisConfig = Field(..., description="Redis Connection Configuration")
    prometheus: Optional[PrometheusConfig] = Field(
        None, description="Optional Prometheus Logging Configuration"
    )
    database: RelationalDatabaseConfig = Field(
        ..., description="Database Connection Configuration"
    )


class RouterConfig(BaseModel):
    """
    Configuration for the LMOS Router which delegates requests to the appropriate service.

    `log_request_dump_max_queue_size` and `log_request_dump_queue_timeout` are used to determine when to insert usage logs into the RDB.
    LMOS Router will queue usage logs internally to prevent delays in the request response cycle.

    It is recommended that you set the `log_request_dump_max_queue_size` such that it frequently triggers prior to reaching the the time limit specified by `log_request_dump_queue_timeout`.
    """

    log_request_dump_max_queue_size: int = Field(
        default=1000,
        description="In number of entries: Threshold for worker to insert usage logs into RDB",
    )
    log_request_dump_queue_timeout: int = Field(
        default=1000,
        description="In Seconds: The max time between worker inserting into RDB",
    )

class Services(BaseModel):
    """
    Configuration for all services.
    """

    router: RouterConfig = Field(
        default_factory=lambda: RouterConfig(),
        description="Configuration for the LMOS Router",
    )
    llm_runner: List[LLM_RUNNERS] = Field(
        default_factory=list, description="List of LLM runner services"
    )
    stt_runner: List[STT_RUNNERS] = Field(
        default_factory=list, description="List of STT runner services"
    )
    tts_runner: List[TTS_RUNNERS] = Field(
        default_factory=list, description="List of TTS runner services"
    )
    rerank_runner: List[RERANK_RUNNERS] = Field(
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
    services: Services = Field(..., description="Service configurations")

    model_config = ConfigDict(
        title="Global LMOS Config",
    )
