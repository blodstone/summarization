import os
from typing import Callable
from pyrouge import Rouge155
from module.base_module import BaseModule
from module.context.evaluator_context import EvaluatorContext
from module.reader.base_reader import BaseReader
from structure.cluster import Cluster
from structure.document import Document


class RougeModule(BaseModule):

    def __init__(self, context: EvaluatorContext):
        self._context = context
        self.r = None
        self.set_up()

    def set_up(self):
        rouge_dir = '/opt/ROUGE'
        rouge_args = '-e /opt/ROUGE/data -m -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -a'
        self.r = Rouge155(rouge_dir, rouge_args)
        self.r.model_dir = os.path.join(self._context.output_path, self._context.category, 'gold')
        self.r.system_dir = os.path.join(
            self._context.output_path, self._context.category, 'summary', self._context.iter_name)
        if not os.path.isdir(self.r.model_dir) and not os.path.isdir(self.r.system_dir):
            raise Exception('Either gold or system folder has not been generated')
        if self._context.dataset == BaseReader.Type.AMR:
            self.r.model_filename_pattern = 'PROXY_[A-Z]{3}_ENG_#ID#'
            self.r.system_filename_pattern = 'PROXY_[A-Z]{3}_ENG_([0-9_]+).system'

    def get_command(self) -> Callable:
        return self._evaluate

    def _evaluate(self, cluster: Cluster)->Cluster:
        rouge_output = self.r.convert_and_evaluate()
        result = self.r.output_to_dict(rouge_output)
        setattr(cluster, 'rouge', result)
        return cluster
