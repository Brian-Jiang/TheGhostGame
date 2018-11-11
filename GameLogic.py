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
        if winner == 0: print('You ', end='')
        else: print('AI ', end='')
        print('won, score is\tyou', self.score[0], self.score[1], 'AI')
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
        print('Game end, the winner is', end='')
        if winner == 0: print(' you!!')
        else: print(' AI!')
        print('\nThank you for Playing the Ghost Game.')

    def _clear_board(self):
        self.word = ''
        self.turn = randrange(0,2)

    def _check_prefix(self, prefix):
        return find_prefix(prefix, self.words)

