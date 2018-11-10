class GhostGame:
    def __init__(self):
        self.score = (0, 0)  # human : computer
        self.word = []
        self.chance = 3
        self.turn = 0  # 0: human   1: computer



    def end_round(self, winner: 'int, 0 or 1'):
        self.score[winner] += 1
        if self.score[winner] >= 5:
            self.end_game(winner)
        else:
            self._clear_board()

    def end_game(self, winner: 'int, 0 or 1'):
        pass

    def _clear_board(self):
        self.word = []
        self.chance = 3