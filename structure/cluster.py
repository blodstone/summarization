from typing import Iterator
from collections.abc import Mapping
from structure.document import Document


class Cluster(Mapping):

    def __init__(self):
        self._documents = dict()

    def __iter__(self) -> Iterator:
        return self._documents.__iter__()

    def __len__(self) -> int:
        return self._documents.__len__()

    def __getitem__(self, doc_id):
        if doc_id not in self._documents.keys():
            self._documents[doc_id] = Document()
            self._documents[doc_id].id = doc_id
        return self._documents[doc_id]
