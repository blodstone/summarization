from typing import Optional, Sequence

from module.context.base_context import BaseContext


class UtilContext(BaseContext):

    def __init__(self, args: Optional[Sequence[str]]):
        super().__init__(args)
        self._output_path = ''
        self._category = ''
        self._iter_name = ''
        self._service = ''

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, new_service):
        self._service = new_service

    @property
    def iter_name(self):
        return self._iter_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        self._category = new_category

    @property
    def output_path(self):
        return self._output_path

    def parse_args(self):
        self._output_path = self._args.output_path
        params = self._get_params(self._args.method)
        self._iter_name = self._gen_iter_name(params)

    def _get_params(self, method: str)->dict:
        params = dict()
        if method == 'lead':
            params['n_lines'] = self._args.n_lines
        return params

    def _gen_iter_name(self, params: dict)->str:
        name = self._args.method
        for key, value in params.items():
            name += f'_{key}_{value}'
        return name