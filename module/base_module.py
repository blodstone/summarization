from abc import ABC, abstractmethod
from typing import Callable

from structure.cluster import Cluster


class BaseModule(ABC):

    @abstractmethod
    def set_up(self):
        raise NotImplementedError

    def get_command(self) -> Callable:
        return self.command

    @abstractmethod
    def add_module_code(self, cluster: Cluster) -> Cluster:
        raise NotImplementedError

    def command(self, cluster) -> Cluster:
        self.set_up()
        return self.add_module_code(cluster)
