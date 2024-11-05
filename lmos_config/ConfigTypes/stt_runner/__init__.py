from typing import Annotated, Union

from pydantic import Field
from ..generic.service import ExternalService
from .faster_whisper import FasterWhisper

STT_RUNNERS = Annotated[
    Union[FasterWhisper, ExternalService], Field(discriminator='type')
]