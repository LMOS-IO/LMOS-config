from pydantic import BaseModel, Field

from .redis import RedisConfig
from .relational_database import RelationalDatabaseConfig

class InternalConfiguration(BaseModel):
    """
    Config for services LMOS depends on.
    """

    redis: RedisConfig = Field(
        ..., description="Redis Connection Configuration"
    )
    database: RelationalDatabaseConfig = Field(
        ..., description="Database Connection Configuration"
    )