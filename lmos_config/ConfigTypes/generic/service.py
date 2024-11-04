from typing import List, Literal, Optional
from pydantic import AnyUrl, BaseModel, computed_field, Field
from functools import cached_property
import re

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

    _port: int = 80
    @computed_field # type: ignore[prop-decorator]
    @cached_property
    def endpoint(self) -> str:
        name=re.sub(r'[^a-z0-9-]', '-', self.name)
        return f"http://{name}:{self._port}/v1"


class ExternalService(GenericServiceConfig):
    """
    Config for external services
    """

    type: Literal["external"]
    api_key: Optional[str] = Field(None, description="Optional API key for the service")
    endpoint: AnyUrl = Field(..., description="Optional endpoint URL for the service")
