import uuid

class Token:

    def __init__(self):
        self._id = uuid.uuid4()
        self._pos = 0
        self._word = ''

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, new_word):
        self._word = new_word

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new_pos):
        self._pos = new_pos