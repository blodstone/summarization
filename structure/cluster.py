from typing import Iterator
from collections.abc import Mapping
from structure.document import Document


class Cluster(Mapping):

    def __init__(self):
        self._documents = dict()
        self._module_codes = list()

    @property
    def module_codes(self):
        return self._module_codes

    def append_code(self, code: str):
        self._module_codes.append(code)

    def __iter__(self) -> Iterator:
        return self._documents.__iter__()

    def __len__(self) -> int:
        return self._documents.__len__()

    def __getitem__(self, doc_id):
        if doc_id not in self._documents.keys():
            self._documents[doc_id] = Document()
            self._documents[doc_id].id = doc_id
        return self._documents[doc_id]
