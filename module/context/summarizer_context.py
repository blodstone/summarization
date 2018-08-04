from typing import Optional, Sequence
from module.context.base_context import BaseContext


class SummarizerContext(BaseContext):

    def __init__(self, args: Optional[Sequence[str]]):
        super().__init__(args)
        self._method = ''
        '''Lead Parameter'''
        self._n_lines = 0

    @property
    def method(self):
        return self._method

    def parse_args(self):
        self._method = self._args.method
        if self._method == 'lead':
            self._n_lines = self._args.n_lines

    def get_lead_parameters(self)->dict:
        if self._method != 'lead':
            raise Exception('Function and method does not match.')
        params = dict()
        if self._n_lines:
            params['n_lines'] = self._n_lines
        else:
            raise Exception('N_lines hyper-parameter is required.')
        return params
