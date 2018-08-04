from typing import Callable
from module.context.preprocessor_context import PreprocessorContext
from module.base_module import BaseModule
from structure.cluster import Cluster
from structure.document import Document
from structure.sentence import Sentence
from structure.token import Token
from library.corenlp import CoreNLP


class CoreNLPModule(BaseModule):

    def __init__(self, context: PreprocessorContext):
        self._context = context
        self._nlp = None

    def add_module_code(self, cluster: Cluster) -> Cluster:
        if self._context.annotation == 'tokenize':
            cluster.append_code('tokenize')
        elif self._context.annotation == 'pos-tag':
            cluster.append_code('pos-tag')
        elif self._context.annotation == 'dependency':
            cluster.append_code('dependency')
        return cluster

    def command(self, cluster):
        cluster = super().command(cluster)
        return self._annotate(cluster)

    def set_up(self):
        self._nlp = CoreNLP(corenlp_path=self._context.corenlp_path).nlp

    def _annotate(self, cluster: Cluster):
        doc_id: str
        doc: Document
        for doc_id, doc in cluster.items():
            sent: Sentence
            for sent in doc.bodies:
                if self._context.annotation == 'tokenize':
                    self._tokenize(sent)
                elif self._context.annotation == 'pos-tag':
                    self._pos_tag(sent)
                elif self._context.annotation == 'dependency':
                    self._parse_dep(sent)
        return cluster

    def _tokenize(self, sent: Sentence):
        tokens = self._nlp.word_tokenize(sent.text)
        sent.tokens = list()
        for t in tokens:
            token = Token()
            token.word = t
            token.pos = len(sent.tokens)
            sent.tokens.append(token)

    def _pos_tag(self, sent: Sentence):
        tokens = self._nlp.pos_tag(sent.text)
        sent.tokens = list()
        for t in tokens:
            token = Token()
            token.word = t[0]
            token.pos = len(sent.tokens)
            setattr(token, 'POStag', t[1])
            sent.tokens.append(token)

    def _parse_dep(self, sent: Sentence):
        dep_arcs = [(arc[0], arc[1]-1, arc[2]-1) for arc in self._nlp.dependency_parse(sent.text)]
        setattr(sent, 'dep_arcs', dep_arcs)
