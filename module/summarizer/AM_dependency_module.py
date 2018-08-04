from typing import Callable, Any

from module.base_module import BaseModule
from module.context.summarizer_context import SummarizerContext
from structure.cluster import Cluster
from structure.document import Document


class AMDependency(BaseModule):

    def __init__(self, context: SummarizerContext):
        self._context = context

    def get_command(self) -> Callable:
        pass

    def set_up(self):
        pass

    def _summarize(self, cluster: Cluster)->Cluster:
        doc_id: str
        doc: Document
        for doc_id, doc in cluster.items():
            combined_doc = self._combine_document(doc)
            summ_doc = self._extract_summ_doc(combined_doc)
            summary = self._generate_summ(summ_doc)
            setattr(doc, 'summary', summary)
        return cluster

    def _combine_document(self, document: Document)->Any:
        pass