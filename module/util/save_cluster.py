import os
from typing import Callable

from module.base_module import BaseModule
from module.context.util_context import UtilContext
from structure.cluster import Cluster


class SaveCluster(BaseModule):

    def __init__(self, context: UtilContext):
        self._context = context

    def add_module_code(self, cluster: Cluster) -> Cluster:
        return cluster

    def set_up(self):
        pass

    def _save_cluster(self, cluster: Cluster) -> Cluster:
        self.folder = os.path.join(self._context.output_path, self._context.category,
                                   'summary', self._context.iter_name)
        return cluster
