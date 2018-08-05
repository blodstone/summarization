from library.singleton import Singleton
from stanfordcorenlp import StanfordCoreNLP


class CoreNLP(metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, '_nlp'):
            self._nlp = StanfordCoreNLP(kwargs['corenlp_path'])

    @property
    def nlp(self):
        return self._nlp

    def close(self):
        self._nlp.close()
