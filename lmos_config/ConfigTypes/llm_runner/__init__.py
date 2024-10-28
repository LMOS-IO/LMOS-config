

from typing import Annotated, Literal, Union

from pydantic import Field
from ..generic.service import InternalService, ExternalService


class ExllamaV2Runner(InternalService):
    """ExllamaV2 runner config"""
    type: Literal["exl2"]


LLM_RUNNERS = Annotated[Union[ExllamaV2Runner, ExternalService], Field(discriminator="type")]