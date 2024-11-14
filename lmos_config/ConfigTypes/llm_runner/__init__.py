from typing import Annotated, Union

from pydantic import Field
from ..generic.service import ExternalService
from .exllama import ExllamaV2Runner
from .vllm import vLLMRunner
from .aphrodite import AphroditeRunner  # noqa: F401
from .sglang import SglangRunner


LLM_RUNNERS = Annotated[
    Union[
        ExllamaV2Runner, 
        vLLMRunner, 
        SglangRunner, 
        # AphroditeRunner, # FIXME: this is broken 
        ExternalService,
    ],
    Field(discriminator="type"),
]
