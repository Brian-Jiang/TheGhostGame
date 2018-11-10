import random
class AI:
    def __init__(self, mode:num): #easy:0, medium: 1, hard: 2
        if mode == 0:
            self.mode = 10
        else if mode == 1:
            self.mode = 40
        else:
            self.mode = 80

        
def AI(current_word):
    challenge_det = random.randrange(0,100)
    if challenge_det >=0 and challenge_det <10:
        challenge_det = True
    else:
        challenge_det = False

    