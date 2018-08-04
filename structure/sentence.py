import uuid
from structure.token import Token

class Sentence:

    def __init__(self):
        self._id = uuid.uuid4()
        self._text = ''
        self._tokens = list()
        self._pos = 0

    @property
    def tokens(self)->list:
        return self._tokens

    @tokens.setter
    def tokens(self, new_tokens):
        self._tokens = new_tokens

    @property
    def text(self)->str:
        return self._text

    @text.setter
    def text(self, string:str):
        self._text = string

    @property
    def pos(self)->int:
        return self._pos

    @pos.setter
    def pos(self, new_pos:int):
        self._pos = new_pos