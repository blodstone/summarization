from typing import Optional, Sequence, Union

from module.context.evaluator_context import EvaluatorContext
from module.context.reader_context import ReaderContext
from module.context.preprocessor_context import PreprocessorContext
from module.context.summarizer_context import SummarizerContext
from module.base_module import BaseModule
from module.context.util_context import UtilContext
from module.module_factory import ModuleFactory

class AutoModuleGenerator:

    def __init__(self, category):
        self._contexts = None
        self._category = category

    def set_up_context(self, args: Optional[Sequence[str]]):
        self._contexts = dict()
        self._contexts['reader'] = ReaderContext(args)
        self._contexts['reader'].category = self._category
        self._contexts['reader'].parse_args()
        for annotation in ['pos-tag', 'dependency']:
            self._contexts[annotation] = PreprocessorContext(args)
            self._contexts[annotation].parse_args()
            self._contexts[annotation].annotation = annotation
        self._contexts['summarizer'] = SummarizerContext(args)
        self._contexts['summarizer'].parse_args()
        self._contexts['util'] = UtilContext(args)
        self._contexts['util'].category = self._category
        self._contexts['util'].parse_args()
        self._contexts['evaluator'] = EvaluatorContext(args)
        self._contexts['evaluator'].category = self._category
        self._contexts['evaluator'].parse_args()

    def gen_modules(self)->list:
        modules = list()
        reader = self._gen_reader()
        modules.extend(reader)
        preprocessors = self._gen_preprocessors()
        modules.extend(preprocessors)
        # if self._category in ['dev', 'test']:
        #     summarizer = self._gen_summarizer()
        #     modules.extend(summarizer)
        #     print_gold_summary = self._gen_util('print_gold_summary')
        #     modules.extend(print_gold_summary)
        #     print_summary = self._gen_util('print_summary')
        #     modules.extend(print_summary)
        #     evaluators = self._gen_evaluators()
        #     modules.extend(*evaluators)
        return modules

    def _gen_reader(self)->list:
        modules = list()
        modules.append(ModuleFactory.create_reader(self._contexts['reader']))
        return modules

    def _gen_preprocessors(self)->list:
        modules = list()
        for annotation in ['pos-tag', 'dependency']:
            modules.append(ModuleFactory.create_corenlp_preprocessor(self._contexts[annotation]))
        return modules

    def _gen_summarizer(self)->list:
        modules = list()
        modules.append(ModuleFactory.create_summarizer(self._contexts['summarizer']))
        return modules

    def _gen_util(self, service)->list:
        modules = list()
        self._contexts['util'].service = service
        modules.append(ModuleFactory.create_util(self._contexts['util']))
        return modules

    def _gen_evaluators(self)->list:
        modules = list()
        modules.append(ModuleFactory.create_evaluators(self._contexts['evaluator']))
        return modules
