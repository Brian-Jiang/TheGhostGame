from GameLogic import GhostGame
from GameAI import AI
from _Helper import *

alpha = 'qazwsxedcrfvtgbyhnujmikolp'


if __name__ == '__main__':
    word_bank = get_word_bank()
    game = GhostGame(word_bank)
    difficulty = int(input('Please choose a difficulty\n'
                           '0: easy\t\t1: medium\t  2: hard\n'))
    ai = AI(difficulty, alpha, word_bank)
    print('Welcome to the Ghost Game, you are facing a', end='')
    if difficulty == 0: print('n easy ghost AI.')
    if difficulty == 1: print(' medium ghost AI!')
    if difficulty == 2: print(' crazy ghost AI!!!')
    while game.turn != -1:
        # print('the current word is ' + game.word)
        if game.turn == 0:
            if game.word == '': print('Please enter your first character: ')
            else: print('The current word is:',  game.word,
                        '\nPlease enter your next character: ')
            guess = input()[0]
            game.guess_char(guess)
            if len(game.word) >= 4:
                game.check_complete()
            if ai.challenge(game.word) and len(game.word) >= 4:
                print('AI is challenging you!')
                game.challenge()
            else:
                game.proceed()
        elif game.turn == 1:
            print('Now is AI\'s turn.')
            guess = ai.return_word(game.word)
            # print('AI guess', guess)
            game.guess_char(guess)
            print('AI guessed', guess)

            if len(game.word) >= 4:
                game.check_complete()
            if len(game.word) >= 4:
                user_c = input("Do you want to challenge AI? (y for yes, other for no)\n")  # 'y' or 'n'
                if user_c == "y":
                    game.challenge()
                else:
                    game.proceed()
            else:
                game.proceed()
