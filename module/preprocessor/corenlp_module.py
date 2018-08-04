from typing import Callable
from module.context.preprocessor_context import PreprocessorContext
from module.base_module import BaseModule
from structure.cluster import Cluster
from structure.document import Document
from structure.sentence import Sentence
from structure.token import Token
from library.corenlp import CoreNLP

class CoreNLPModule(BaseModule):

    def __init__(self, context:PreprocessorContext):
        self._context = context
        self._nlp = CoreNLP(corenlp_path=self._context.corenlp_path).nlp

    def get_command(self) -> Callable:
        return self._annotate

    def set_up(self):
        pass

    def _annotate(self, cluster: Cluster):
        doc_id: str
        doc: Document
        for doc_id, doc in cluster.items():
            sent: Sentence
            for sent in [*doc.bodies, *[sent for ex in doc.gold_summaries for sent in ex.sentences]]:
                if self._context.annotation == 'tokenize':
                    self._tokenize(sent)
                elif self._context.annotation == 'pos-tag':
                    self._pos_tag(sent)
        return cluster

    def _tokenize(self, sent):
        tokens = self._nlp.word_tokenize(sent.text)
        sent.tokens = list()
        for t in tokens:
            token = Token()
            token.word = t
            token.pos = len(sent.tokens)
            sent.tokens.append(token)


    def _pos_tag(self, sent):
        tokens = self._nlp.pos_tag(sent.text)
        sent.tokens = list()
        for t in tokens:
            token = Token()
            token.word = t[0]
            token.pos = len(sent.tokens)
            setattr(token, 'POStag', t[1])
            sent.tokens.append(token)