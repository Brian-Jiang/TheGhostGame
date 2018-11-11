from GameLogic import GhostGame
from GameAI import AI
from _Helper import *
import time
from GameGUI import GameBoard

alpha = 'qazwsxedcrfvtgbyhnujmikolp'


class controller:

    def __int__(self, mode):
        self.word_bank = get_word_bank()
        self.game = GhostGame(self.word_bank)
        self.ai = AI(mode, alpha, self.word_bank)
        self.userScore = self.game.score[0]
        self.AIScore = self.game.score[1]



    def func(self, word):#take a word
        time.sleep(1)
        if self.ai.challenge(word):
            return '_'
        else:
            result = self.ai.return_word(word)
            return result
