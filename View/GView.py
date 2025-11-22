import tkinter as tk

class GView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.geometry("500x475")
        self.root.title("Hangman Game")

        self.stage_count = 0
        self.stages = ['''
                +-----+
                |     |
                      |
                      |
                      |
                      |
                =========''', '''
                +-----+
                |     |
                O     |
                      |
                      |
                      |
                =========''', '''
                +-----+
                |     |
                O     |
                |     |
                      |
                      |
                =========''', '''
                +-----+
                |     |
                O     |
               /|     |
                      |
                      |
                =========''', '''
                +-----+
                |     |
                O     |
               /|\\    |
                      |
                      |
                =========''', '''
                +-----+
                |     |
                O     |
               /|\\    |
               /      |
                      |
                =========''', '''
                +-----+
                |     |
                O     |
               /|\\    |
               / \\    |
                      |
                ========='''
            ]

        self.labelStage = tk.Label(self.root, text=self.stages[self.stage_count], font=('Courier', 14), width=24, justify="left")
        self.labelStage.pack(pady=(0,10), padx=(0,80))

        self.labelWord = tk.Label(self.root, text="", font=('Arial', 14), bg = "whitesmoke")
        self.labelWord.pack()

    def start(self):
        self.root.mainloop()