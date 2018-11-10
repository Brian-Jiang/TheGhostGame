import random
def AI(current_word):
    challenge_det = random.randrange(0,100)
    if challenge_det >=0 and challenge_det <10:
        challenge_det = True
    else:
        challenge_det = False