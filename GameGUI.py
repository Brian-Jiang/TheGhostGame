import tkinter
from tkinter import *
from PIL import Image, ImageTk
from controller import *
DEFAULT_FONT = ('Herculanum', 24)
from time import sleep

class GameBoard:
    def __init__(self):
        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Menu")
        self._dialog.geometry("700x523")
        self._dialog.configure(background = '#F16F29')
        # image = PhotoImage(file='Hallowen-Background.png')
        self.image = Image.open("Hallowen-Background.png")
        self.image = ImageTk.PhotoImage(self.image)
        label = Label(self._dialog, image=self.image)
        label.image = self.image
        label.pack()
        label.place(x=0, y=0, relwidth=1, relheight=1)
        self._title = tkinter.Label(
            master = self._dialog, text = "Ghost Game",
            font =  ('Old Europe', 48), background = '#F06824'
        )
        self._title.grid(
            row = 0, column = 1, columnspan = 3, padx = 20, pady = 20,
            sticky = tkinter.N
        )

        self._button_frame = tkinter.Frame(master = self._dialog, background = '#F27E35')
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
        self._dialog.attributes("-topmost", True)
        self._dialog.resizable(False,False)
    def _easyCommand(self):
        self._dialog.destroy()
        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Easy Mode")
        self._dialog.geometry("700x523")

        self.image = Image.open("Hallowen-Background.png")
        self.image = ImageTk.PhotoImage(self.image)
        label = Label(self._dialog, image=self.image)
        label.image = self.image
        label.pack()
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.startGame(3)

    def _mediumCommand(self):
        self._dialog.destroy()
        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Medium Mode")
        self._dialog.geometry("700x523")

        self.image = Image.open("Hallowen-Background.png")
        self.image = ImageTk.PhotoImage(self.image)
        label = Label(self._dialog, image=self.image)
        label.image = self.image
        label.pack()
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.startGame(4)

    def _hardCommand(self):
        self._dialog.destroy()
        self._dialog = tkinter.Tk()
        self._dialog.title("Ghost Game Hard Mode")
        self._dialog.geometry("700x523")

        self.image = Image.open("Hallowen-Background.png")
        self.image = ImageTk.PhotoImage(self.image)
        label = Label(self._dialog, image=self.image)
        label.image = self.image
        label.pack()
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.startGame(5)

    def _exitCommand(self):
        self._dialog.destroy()

    def _restartCommand(self):
        self._dialog.destroy()
        self.__init__()

    def _on_canvas_revized(self, event: tkinter.Event):
        pass

    def get_key(self, event):
        self.canvas.delete(tkinter.ALL)
        self.vocb += event.char
        self.canvas.text = self.canvas.create_text(250, 70, anchor='w', text= self.vocb)
        if not find_prefix(self.vocb, self.control.word_bank):
            self.control.AIScore += 1
            self.g_score.set(f'Ghost {self.control.AIScore}')
            self.vocb = ''
            return
        if check_complete_word(self.vocb, self.control.word_bank):
            self.control.AIScore += 1
            self.g_score.set(f'Ghost {self.control.AIScore}')
            self.vocb = ''
            return
        self.canvas.text = self.canvas.create_text(250, 70, anchor='w', text= self.vocb)

        result = self.control.turn(self.vocb)
        if result == '_':
            self.control.AIScore += 1
            self.g_score.set(f'Ghost {self.control.AIScore}')
            self.vocb = ''
            return
        else:
            self.vocb+=result
            self.canvas.delete(tkinter.ALL)
            self.canvas.text = self.canvas.create_text(250, 70, anchor='w', text= self.vocb)
            sleep(2)
            if not find_prefix(self.vocb, self.control.word_bank):
                self.control.UserScore += 1
                self.h_score.set(f'User {self.control.UserScore}')
                self.vocb = ''
                return
            if check_complete_word(self.vocb, self.control.word_bank) find_prefix(self.vocb, self.control.word_bank):
                self.control.UserScore += 1
                self.h_score.set(f'User {self.control.UserScore}')
                self.vocb = ''
                return
            


    def startGame(self, mode:int): #E3, M4, H5
        self.control = controller(mode)
        self.g_score = tkinter.StringVar()
        self.h_score = tkinter.StringVar()
        self.g_score.set(f'Ghost {self.control.AIScore}')
        self.h_score.set(f'User {self.control.UserScore}')
        self.vocb = ''
        self._title = tkinter.Label(
            master = self._dialog, text = "Ghost Game",
            font =  ('Old Europe', 48), background = '#F06824'
        )
        
        self._title.grid(
            row = 0, column = 0, columnspan = 3, padx = 20, pady = 20,
            sticky = tkinter.N
        )
        
        button_frame = tkinter.Frame(master = self._dialog, background = '#F06824')
        button_frame.grid(
            row = 0, column = 2, padx = 8, pady = 20,
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

        self.canvas = tkinter.Canvas(
            master = self._dialog, width = 500, height = 200,
            background = 'orange',
        )
    
        self.canvas.grid(
            row = 1 , column = 0,
            sticky = tkinter.W + tkinter.E + tkinter.N + tkinter.S

        )
        self.canvas.bind("<Configure>", self._on_canvas_revized)
        score_board = tkinter.Frame(
            master = self._dialog, background = '#F16F29'
        )
        score_board.grid(
            row = 0 , column = 0, padx = 20, pady = 20,
            sticky = tkinter.W+tkinter.N
        )
        score_H = tkinter.Label(
            master = score_board, textvariable= self.h_score,
            font = DEFAULT_FONT, background = '#F16F29',
            )
        score_H.grid(
            row = 0, column = 0, columnspan = 3, padx = 20, pady = 20,
        )
        score_G = tkinter.Label(
            master = score_board, textvariable = self.g_score,
            font = DEFAULT_FONT, background = '#F16F29'
            )
        score_G.grid(
            row = 1, column = 0, columnspan = 3, padx = 20, pady = 20,
        )
        self.g_image = Image.open("ghost_picture.jpg")
        self.g_image = ImageTk.PhotoImage(self.g_image)
        ghost_l = Label(master = button_frame, image=self.g_image)
        # ghost_l.image = self.g_image
        # ghost_l.pack()
        ghost_l.grid(
            row=2, column=0, columnspan=3, padx=8, pady=20,
        )
        # ghost_l.place(x=0, y=0, relwidth=1, relheight=1)


        self._dialog.bind('<Key>', self.get_key)
        
        self._dialog.rowconfigure(5, weight = 1)
        self._dialog.columnconfigure(1, weight = 1)

            
        
    
if __name__ == '__main__':
    board = GameBoard()
    board._dialog.mainloop()
