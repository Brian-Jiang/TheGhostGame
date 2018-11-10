from GameLogic import GhostGame
from GameAI import AI
from _Helper import *

alpha = 'qazwsxedcrfvtgbyhnujmikolp'


if __name__ == '__main__':
    word_bank = get_word_bank()
    game = GhostGame(word_bank)
    ai = AI(1, alpha, word_bank)
    while game.turn != -1:
        print('the current word is ' + game.word)
        if game.turn == 0:
            guess = input("guess a character: ")[0]
            game.guess_char(guess)
            if len(game.word) >= 4:
                game.check_complete()
            else:
                if ai.challenge(game.word) and len(game.word) >= 4:
                    print('AI challenge')
                    game.challenge()
                else:
                    print('AI not challenge')
                    game.proceed()
        elif game.turn == 1:
            print('AI\'s turn')
            guess = ai.return_word(game.word)
            print('AI guess', guess)
            game.guess_char(guess)
            if len(game.word) >= 4:
                game.check_complete()
            else:
                if len(game.word) >= 4:
                    user_c = input("challenge or not ?  ")  # 'y' or 'n'
                    if user_c == "y":
                        game.challenge()
                    else:
                        game.proceed()
                else:
                    game.proceed()
