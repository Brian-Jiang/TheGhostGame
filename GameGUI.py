import tkinter
from tkinter import *
from PIL import Image, ImageTk

DEFAULT_FONT = ('Herculanum', 24)


class GameBoard:
    def __init__(self):

        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Menu")
        self._dialog.geometry("700x523")
        # image = PhotoImage(file='Hallowen-Background.png')
        image = Image.open("Hallowen-Background.png")
        image = ImageTk.PhotoImage(image)
        label = Label(self._dialog, image=image)
        label.image = image
        label.pack()
        label.place(x=0, y=0, relwidth=1, relheight=1)
        self._title = tkinter.Label(
            master = self._dialog, text = "Ghost Game",
            font =  ('Old Europe', 48)
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
            font = DEFAULT_FONT,
            command = self._easyCommand
        )
        self._easyButton.grid(
            row = 0, column = 0, padx = 10, pady = 10
        )
        self._middleButton = tkinter.Button(
            master = self._button_frame, text = "MIDDIUM",
            font = DEFAULT_FONT,
            command = self._mediumCommand
        )
        self._middleButton.grid(
            row = 1, column = 0, padx = 10, pady = 10
        )
        self._hardButton = tkinter.Button(
            master = self._button_frame, text = "HARD",
            font = DEFAULT_FONT,
            command = self._hardCommand
        )
        self._hardButton.grid(
            row = 2, column = 0, padx = 10, pady = 10
        )

        self._dialog.rowconfigure(5, weight = 1)
        self._dialog.columnconfigure(1, weight = 1)

    def _easyCommand(self):
        self._dialog.destroy()
        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Easy Mode")
        self._dialog.geometry("700x523")
        self.startGame(0)

    def _mediumCommand(self):
        self._dialog.destroy()
        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Medium Mode")
        self.startGame(1)

    def _hardCommand(self):
        self._dialog.destroy()
        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Hard Mode")
        self.startGame(2)

    def startGame(self, mode:int): #E0, M1, H2
        self._title = tkinter.Label(
            master = self._dialog, text = "Ghost Game",
            font =  ('Old Europe', 48)
        )
        
        self._title.grid(
            row = 0, column = 0, columnspan = 3, padx = 20, pady = 20,
            sticky = tkinter.N
        )
        
        button_frame = tkinter.Frame(master = self._dialog)
        button_frame.grid(
            row = 0, column = 2, padx = 20, pady = 20,
            sticky = tkinter.E+tkinter.N
        )

        restart = tkinter.Button(
            master = button_frame, text = "RESTART",
            font = ('Old Europe', 18),
            command = self._restartCommand
        )

        restart.grid(
            row = 0, column = 0, padx = 5, pady = 5
        )
        exit = tkinter.Button(
            master = button_frame, text = "EXIT",
            font = ('Old Europe', 18),
            command = self._exitCommand
        )
        exit.grid(
            row = 1, column = 0, padx = 5, pady = 5    
        )

        canvas = tkinter.Canvas(
            master = self._dialog, width = 500, height = 500,
            background = 'green',
        )
        canvas.grid(
            row = 1 , column = 0,
            sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S

        )
        self._dialog.rowconfigure(5, weight = 1)
        self._dialog.columnconfigure(1, weight = 1)
        
    def _exitCommand(self):
        self._dialog.destroy()

    def _restartCommand(self):
        self._dialog.destroy()
        self.__init__()

if __name__ == '__main__':
    board = GameBoard()
    board._dialog.mainloop()
