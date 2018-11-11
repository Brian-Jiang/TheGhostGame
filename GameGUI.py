import tkinter

DEFAULT_FONT = ('Time', 24)

class GameBoard:
    def __init__(self):
        self._dialog = tkinter.Tk()
        self._title = tkinter.Label(
            master = self._dialog, text = "Ghost Game",
            font = DEFAULT_FONT
        )
        self._title.grid(
            row = 0, column = 0, columnspan = 2, padx = 20, pady = 20,
            sticky = tkinter.N
        )



if __name__ == '__main__':
    GameBoard()
