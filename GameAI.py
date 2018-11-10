import random
from _Helper import *
class AI:
    def __init__(self, mode, aphebet:list, word_bank:set): #easy:0, medium: 1, hard: 2
        self.aphebet = aphebet
        self.word_bank = word_bank
        if mode == 0:
            self.cmode = 10
            self.wmode = 50 #xiaxie
        elif mode == 1:
            self.cmode = 40
            self.wmode = 10 #xiaxie
        else:
            self.cmode = 80
            self.wmode = 0

        
    def _challenge(self):
        challenge_det = random.randrange(0,100)
        if challenge_det >=0 and challenge_det < self.cmode:
            return True
        else:
            return False

    def return_word(self, word): #1:"word_challenge" 2:"newWord"
        if self._challenge():
            return "_"
        else:
            w_det = random.randrange(0,100)
            if w_det < self.wmode:
                return random.choice(self.aphebet) #xiaxuan
            else:
                temp_set = find_prefix(word, self.word_bank)
                return temp_set.pop()[len(word)]
                


    