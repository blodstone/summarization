from typing import Callable
from module.reader.base_reader import BaseReader
from module.base_module import BaseModule
from structure.cluster import Cluster
from module.context.reader_context import ReaderContext
from structure.sentence import Sentence


class AMRReader(BaseReader, BaseModule):

    def __init__(self, context:ReaderContext):
        self._context = context

    def set_up(self):
        pass

    def get_command(self)->Callable:
        return self._load_file

    def _load_file(self, cluster: Cluster)->Cluster:
        snt_text = ''
        snt_id = ''
        snt_type = ''
        amr_string = ''
        file = open(self._context.path, 'r')
        for line in file:
            line = line.rstrip()
            # Every AMR graph is ended by an empty line
            if line == '':
                # This happen on the first line of the file
                if amr_string == '':
                    continue
                else:
                    if snt_type == 'summary' or snt_type == 'body':
                        document = cluster[snt_id]
                        sentence = Sentence()
                        sentence.text = snt_text
                        setattr(sentence, 'amr', amr_string)
                        if snt_type == 'body':
                            document.append_bodies(sentence)
                        else:
                            document.add_gold_summary_example([sentence])
                    amr_string = ''
                    continue

            # Read sentence tokens
            if line.startswith('#'):
                fields = line.split('::')
                for field in fields[1:]:
                    tokens = field.split()
                    if tokens[0] == 'id':
                        snt_id = tokens[1].split('.')[:-1][0]
                    if tokens[0] == 'snt':
                        snt_text = ' '.join(tokens[1:])
                    if tokens[0] == 'snt-type':
                        snt_type = tokens[1]
                continue

            # If line is not start by # and not empty means it's part of AMR graph
            amr_string += line + '\n'
        return cluster

