from GameLogic import GhostGame
from GameAI import AI
from _Helper import *
from GameGUI import GameBoard

alpha = 'qazwsxedcrfvtgbyhnujmikolp'

if __name__ == "__main__":
    word_bank = get_word_bank()
    game = GhostGame(word_bank)
    ai = AI(1, alpha, word_bank)
    board = GameBoard()
    board._dialog.mainloop()