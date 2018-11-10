from GameLogic import GhostGame
from GameAI import AI
from _Helper import *

alpha = 'qazwsxedcrfvtgbyhnujmikolp'

def main():


    while (input() =='continue'):
        game = GhostGame()





if __name__ == '__main__':
    word_bank = get_word_bank()
    game = GhostGame(word_bank)
    ai = AI(1, alpha, word_bank)
    while game.turn != -1:
        print('the current word is ' + game.word)
        if game.turn == 0:
            guess = input("guess a character")[0]
            game.guess_char(guess)
            if ai.challenge():
                game.challenge()
            else:
                pass
        elif game.turn == 1:
            guess = ai.return_word(game.word)
            game.guess_char(guess)
            user_c = input("challenge or not ?")# 'yes' or 'no'
            if user_c == "yes":
                game.challenge()
            else:
                pass
