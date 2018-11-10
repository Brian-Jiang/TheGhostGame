from _Helper import *
from random import randrange

class GhostGame:
    def __init__(self, word_bank: set):
        self.score = [0, 0]  # human : computer
        self.word = ''
        self.turn = randrange(0,2)  # 0: human   1: computer
        self.words = word_bank

    def guess_char(self, char):
        self.word += char

    def proceed(self):
        self.turn = 0 if self.turn == 1 else 1


    def challenge(self):
        if self._check_prefix(self.word):
            self.end_round(self.turn)
        else:
            self.end_round(0 if self.turn == 1 else 1)


    def end_round(self, winner: 'int, 0 or 1'):
        self.score[winner] += 1
        print('end round, score is', self.score)
        if self.score[winner] >= 5:
            self.end_game(winner)
        else:
            self._clear_board()

    def check_complete(self):
        if check_complete_word(self.word, self.words):
            self.end_round(0 if self.turn == 1 else 1)

    # def check_if_complete_word(self):
    #     result = check_complete_word(self.word, self.words)
    #     return True if result == 1 else False

    def end_game(self, winner: 'int, 0 or 1'):
        self.turn = -1
        print('winner:', winner)
        pass

    def _clear_board(self):
        self.word = ''
        self.turn = randrange(0,2)

    def _check_prefix(self, prefix):
        return find_prefix(prefix, self.words)

