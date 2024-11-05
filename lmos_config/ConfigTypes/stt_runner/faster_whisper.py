from typing import Literal
from ..generic.service import InternalService


class FasterWhisper(InternalService):
    """FasterWhisper runner config"""

    type: Literal["fasterwhisper"]
