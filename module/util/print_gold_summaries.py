import os
from typing import Callable

from module.base_module import BaseModule
from module.context.util_context import UtilContext
from structure.cluster import Cluster
from structure.document import Document, Example


class PrintGoldSummaries(BaseModule):

    def __init__(self, context: UtilContext):
        self._context = context
        self.folder = ''
        self.set_up()

    def set_up(self):
        self.folder = os.path.join(self._context.output_path, self._context.category, 'gold')
        if not os.path.isdir(self.folder):
            os.makedirs(self.folder)

    def get_command(self) -> Callable:
        return self._gen_summaries

    def _gen_summaries(self, cluster: Cluster)->Cluster:
        doc_id: int
        doc: Document
        for doc_id, doc in cluster.items():
            file_name = f'{doc_id}'
            file = open(os.path.join(self.folder, file_name), 'w')
            result = ''
            example: Example
            for example in doc.gold_summaries:
                result += ' '.join([sent.text for sent in example.sentences]) + '\n'
            file.write(result.strip())
            file.close()
        return cluster

