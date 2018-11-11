from GameLogic import GhostGame
from GameAI import AI
from _Helper import *
import time
from GameGUI import GameBoard

alpha = 'qazwsxedcrfvtgbyhnujmikolp'


class controller:

    def __init__(self, mode):
        self.word_bank = get_word_bank()
        self.game = GhostGame(self.word_bank)
        self.ai = AI(mode, alpha, self.word_bank)
        self.UserScore = 0
        self.AIScore = 0



    def turn(self, word):#take a word
        time.sleep(2)
        if self.ai.challenge(word):
            return '_'
        else:
            result = self.ai.return_word(word)
            return result
