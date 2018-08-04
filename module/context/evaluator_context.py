from typing import Optional, Sequence

from module.context.util_context import UtilContext
from module.reader.base_reader import BaseReader


class EvaluatorContext(UtilContext):

    def __init__(self, args: Optional[Sequence[str]]):
        super().__init__(args)
        self._metrics = list()
        self._dataset = 0

    @property
    def dataset(self):
        return self._dataset

    @property
    def metrics(self):
        return self._metrics

    def parse_args(self):
        super().parse_args()
        if self._args.rouge:
            self._metrics.append('rouge')
        if self._args.amr:
            self._dataset = BaseReader.Type.AMR
