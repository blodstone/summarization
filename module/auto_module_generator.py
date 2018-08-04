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
        self._contexts['preprocessor'] = PreprocessorContext(args)
        self._contexts['preprocessor'].parse_args()
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
        modules.append(reader)
        preprocessors = self._gen_preprocessors()
        modules.append(*preprocessors)
        if self._category in ['dev', 'test']:
            summarizer = self._gen_summarizer()
            modules.append(summarizer)
            print_gold_summary = self._gen_util('print_gold_summary')
            modules.append(print_gold_summary)
            print_summary = self._gen_util('print_summary')
            modules.append(print_summary)
            evaluators = self._gen_evaluators()
            modules.append(*evaluators)
        return modules

    def _gen_reader(self)->Union[BaseModule]:
        return ModuleFactory.create_reader(self._contexts['reader'])

    def _gen_preprocessors(self)->list:
        self._contexts['preprocessor'].annotation = 'pos-tag'
        pos_tagger = ModuleFactory.create_corenlp_preprocessor(self._contexts['preprocessor'])
        return [pos_tagger]

    def _gen_summarizer(self)->BaseModule:
        return ModuleFactory.create_summarizer(self._contexts['summarizer'])

    def _gen_util(self, service)->BaseModule:
        self._contexts['util'].service = service
        return ModuleFactory.create_util(self._contexts['util'])

    def _gen_evaluators(self)->list:
        return ModuleFactory.create_evaluators(self._contexts['evaluator'])
