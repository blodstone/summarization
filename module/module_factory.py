from typing import Union
from module.base_module import BaseModule
from module.context.evaluator_context import EvaluatorContext
from module.context.util_context import UtilContext
from module.evaluator.rouge_module import RougeModule
from module.reader.base_reader import BaseReader
from module.reader.amr_reader import AMRReader
from module.preprocessor.corenlp_module import CoreNLPModule
from module.context.reader_context import ReaderContext
from module.context.preprocessor_context import PreprocessorContext
from module.context.summarizer_context import SummarizerContext
from module.summarizer.lead_line_module import LeadLineModule
from module.util.print_gold_summaries import PrintGoldSummaries
from module.util.print_summaries import PrintSummaries
from module.util.save_cluster import SaveCluster


class ModuleFactory:

    @staticmethod
    def create_reader(context:ReaderContext)->Union[BaseModule]:
        reader = None
        if context.type == BaseReader.Type.AMR:
            reader = AMRReader(context)
        if reader:
            return reader
        else:
            raise NotImplementedError

    @staticmethod
    def create_corenlp_preprocessor(context:PreprocessorContext)->BaseModule:
        return CoreNLPModule(context)

    @staticmethod
    def create_summarizer(context: SummarizerContext)->BaseModule:
        if context.method == 'lead':
            return LeadLineModule(context)

    @staticmethod
    def create_util(context: UtilContext)->BaseModule:
        if context.service == 'print_summary':
            return PrintSummaries(context)
        elif context.service == 'print_gold_summary':
            return PrintGoldSummaries(context)
        elif context.service == 'save_cluster':
            return SaveCluster(context)
        raise Exception('Service not valid for util.')

    @staticmethod
    def create_evaluators(context: EvaluatorContext)->list:
        modules = list()
        if 'rouge' in context.metrics:
            modules.append(RougeModule(context))
        return modules