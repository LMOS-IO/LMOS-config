from typing import Literal
from ..generic.service import InternalService


class ExllamaV2Runner(InternalService):
    """ExllamaV2 runner config"""

    type: Literal["exl2"]
