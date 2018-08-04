from typing import List
from structure.sentence import Sentence


class Document:

    def __init__(self):
        self._id = ''
        self._bodies: List[Sentence] = list()
        self._gold_summaries: List[Example] = list()

    @property
    def gold_summaries(self)->list:
        return self._gold_summaries

    @property
    def bodies(self)->list:
        return self._bodies

    def append_bodies(self, sentence: Sentence):
        sentence.pos = len(self._bodies)
        self._bodies.append(sentence)

    def add_gold_summary_example(self, sentences: List[Sentence]):
        ex = Example()
        sentence: Sentence
        for sentence in sentences:
            sentence.pos = len(ex.sentences)
            ex.append_sentence(sentence)
        self._gold_summaries.append(ex)

class Example:

    def __init__(self):
        self._sentences = list()

    @property
    def sentences(self):
        return self._sentences

    def append_sentence(self, sentence:Sentence):
        self._sentences.append(sentence)