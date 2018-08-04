from typing import Optional, Sequence

from module.context.base_context import BaseContext

class PreprocessorContext(BaseContext):

    def __init__(self, args: Optional[Sequence[str]]):
        super().__init__(args)
        self._corenlp_path = ''
        self._annotation = ''

    @property
    def annotation(self):
        return self._annotation

    @annotation.setter
    def annotation(self, new_annotation):
        self._annotation = new_annotation

    def apply_annotation(self, annotation: str):
        self._annotation = annotation

    @property
    def corenlp_path(self):
        return self._corenlp_path

    def parse_args(self):
        self._corenlp_path = self._args.corenlp_path