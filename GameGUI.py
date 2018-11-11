import tkinter

DEFAULT_FONT = ('Old Europe', 24)

class GameBoard:
    def __init__(self):
        self._dialog = tkinter.Tk()
        self._title = tkinter.Label(
            master = self._dialog, text = "Ghost Game",
            font = DEFAULT_FONT
        )
        self._title.grid(
            row = 0, column = 1, columnspan = 3, padx = 20, pady = 20,
            sticky = tkinter.N
        )

        self._button_frame = tkinter.Frame(master = self._dialog)
        self._button_frame.grid(
            row = 1, column = 1, padx = 40, pady = 40
        )
        self._easyButton = tkinter.Button(
            master = self._button_frame, text = "EASY",
            font = DEFAULT_FONT
            command = self._easyCommand
        )
        self._easyButton.grid(
            row = 0, column = 0, padx = 10, pady = 10
        )
        self._middleButton = tkinter.Button(
            master = self._button_frame, text = "MIDDIUM",
            font = DEFAULT_FONT
        )
        self._middleButton.grid(
            row = 1, column = 0, padx = 10, pady = 10
        )
        self._hardButton = tkinter.Button(
            master = self._button_frame, text = "HARD",
            font = DEFAULT_FONT
        )
        self._hardButton.grid(
            row = 2, column = 0, padx = 10, pady = 10
        )

        self._dialog.rowconfigure(5, weight = 1)
        self._dialog.columnconfigure(1, weight = 1)

    def _easyCommand():


if __name__ == '__main__':
    GameBoard()
