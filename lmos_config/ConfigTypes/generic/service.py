from typing import List, Literal, Optional
from pydantic import AnyUrl, BaseModel, Field


class GenericServiceConfig(BaseModel):
    """
    Generic configuration for services.
    """

    name: str = Field(..., description="Name of the service")
    alias: List[str] = Field(
        default_factory=list, description="List of aliases for the service"
    )


class InternalService(GenericServiceConfig):
    """
    Config for internal services
    """

    location: str = Field(..., description="Path to the model folder or HF repository", serialization_alias="model", validation_alias="model")


class ExternalService(GenericServiceConfig):
    """
    Config for external services
    """

    type: Literal["external"]
    api_key: Optional[str] = Field(None, description="Optional API key for the service")
    endpoint: AnyUrl = Field(..., description="Optional endpoint URL for the service")
