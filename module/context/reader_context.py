from typing import Optional, Sequence
from module.reader.base_reader import BaseReader
from module.context.base_context import BaseContext

class ReaderContext(BaseContext):

    def __init__(self, args: Optional[Sequence[str]]):
        super().__init__(args)
        self._type = None
        self._path = ''
        self._category = ''

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        self._category = new_category

    @property
    def type(self):
        return self._type

    @property
    def path(self):
        return self._path

    def parse_args(self):
        if self._args.amr:
            self._type = BaseReader.Type.AMR
        elif self._args.duc:
            self._type = BaseReader.Type.DUC
        elif self._args.tac:
            self._type = BaseReader.Type.TAC
        if not self._type:
            raise Exception('BaseReader type is unknown.')

        if self._category == '':
            raise Exception('Category is needed.')

        if self._category == 'train':
            self._path = self._args.train_path
        elif self._category == 'dev':
            self._path = self._args.dev_path
        elif self._category == 'test':
            self._path = self._args.test_path
        if not self._path:
            raise Exception('Path is required.')


