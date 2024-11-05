from typing import Annotated, Union

from pydantic import Field
from ..generic.service import ExternalService
from .exllama import ExllamaV2Runner
from .vllm import vLLMRunner
from .aphrodite import AphroditeRunner


LLM_RUNNERS = Annotated[
    Union[ExllamaV2Runner, vLLMRunner, AphroditeRunner, ExternalService],
    Field(discriminator="type"),
]
