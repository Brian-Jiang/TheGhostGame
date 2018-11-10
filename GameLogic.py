class GhostGame:
    def __init__(self):
        self.score = (0, 0)  # human : computer
        self.word = ''
        self.turn = 0  # 0: human   1: computer

    def guess_char(self, char):
        self.word += char

    def proceed(self):
        self.turn = 0 if self.turn == 1 else 1


    def challenge(self):
        if self._check_prefix(self.word):
            self.end_round(self.turn)
        else:
            self.end_round(0 if self.turn == 1 else 1)


    def end_round(self, winner: 'int, 0 or 1'):
        self.score[winner] += 1
        if self.score[winner] >= 5:
            self.end_game(winner)
        else:
            self._clear_board()

    def end_game(self, winner: 'int, 0 or 1'):
        self.turn = -1
        pass

    def _clear_board(self):
        self.word = []

    def _check_prefix(self, prefix):
        pass