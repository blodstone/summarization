from typing import Optional, Sequence
from abc import ABC, abstractmethod


class BaseContext(ABC):

    def __init__(self, args: Optional[Sequence[str]]):
        self._args = args

    @abstractmethod
    def parse_args(self):
        raise NotImplementedError

