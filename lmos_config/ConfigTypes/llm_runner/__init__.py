from typing import Annotated, Union

from pydantic import Field
from ..generic.service import ExternalService
from .exllama import ExllamaV2Runner
from .vllm import vLLMRunner


LLM_RUNNERS = Annotated[
    Union[ExllamaV2Runner, vLLMRunner, ExternalService], Field(discriminator="type")
]
