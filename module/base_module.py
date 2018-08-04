from abc import ABC, abstractmethod
from typing import Callable


class BaseModule(ABC):

    @abstractmethod
    def set_up(self):
        raise NotImplementedError

    @abstractmethod
    def get_command(self) -> Callable:
        raise NotImplementedError
