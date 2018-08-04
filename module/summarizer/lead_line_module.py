from typing import Callable

from module.base_module import BaseModule
from module.context.summarizer_context import SummarizerContext
from structure.cluster import Cluster
from structure.document import Document
from structure.sentence import Sentence


class LeadLineModule(BaseModule):

    def __init__(self, context: SummarizerContext):
        self._context = context
        self._params = None

    def add_module_code(self, cluster: Cluster) -> Cluster:
        cluster.append_code('lead')
        return cluster

    def command(self, cluster):
        cluster = super().command(cluster)
        return self._summarize(cluster)

    def set_up(self):
        self._params = self._context.get_lead_parameters()

    def _summarize(self, cluster: Cluster):
        doc_id: str
        doc: Document
        for doc_id, doc in cluster.items():
            summary = list()
            sentence: Sentence
            for sentence in doc.bodies[:self._params['n_lines']]:
                summary_sent = Sentence()
                summary_sent.text = sentence.text
                summary_sent.pos = len(summary)
                summary.append(summary_sent)
            setattr(doc, 'summary', summary)
        return cluster



