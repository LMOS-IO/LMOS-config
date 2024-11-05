from typing import Annotated, Union

from pydantic import Field
from ..generic.service import ExternalService

TTS_RUNNERS = Annotated[
    Union[ExternalService], Field(discriminator='type')
]