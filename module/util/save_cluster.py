import os
import pickle
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
        self.folder = os.path.join(self._context.output_path, self._context.category,
                                   'cluster', self._context.iter_name)
        if not os.path.isdir(self.folder):
            os.makedirs(self.folder)

    def command(self, cluster):
        cluster = super().command(cluster)
        return self._save_cluster(cluster)

    def _save_cluster(self, cluster: Cluster) -> Cluster:
        file_name = os.path.join(self.folder, '_'.join(cluster.module_codes) + '.pickle')
        file = open(file_name, 'wb')
        pickle.dump(cluster, file)
        file.close()
        return cluster
