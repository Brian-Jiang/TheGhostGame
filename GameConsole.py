from GameLogic import GhostGame
def main():


    while (input() =='continue'):
        game = GhostGame()





if __name__ == '__main__':
    game = GhostGame()
    while game.turn != -1:
        game.guess_char('a')
        game.challenge()
