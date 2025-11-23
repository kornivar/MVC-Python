import tkinter as tk

class GView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.geometry("500x475")
        self.root.title("Hangman Game")

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

        self.labelStage = tk.Label(self.root, text=self.stages[0], font=('Courier', 14), width=24, justify="left")
        self.labelStage.pack(pady=(0,10), padx=(0,80))

        self.labelWord = tk.Label(self.root, text="", font=('Arial', 14))
        self.labelWord.pack(pady=10)

        self.labelAttempts = tk.Label(self.root, text="", font=('Arial', 12))
        self.labelAttempts.pack(pady=10)

        self.entryLetter = tk.Entry(self.root, font=("Arial", 16), width=3)
        self.entryLetter.pack(pady=10)

        self.btnCheck = tk.Button(self.root, text="Check", width=6, height=2, command=self.controller.display_letter)
        self.btnCheck.pack(pady=10)

        self.btnRestart = tk.Button(self.root, text="Get me another one!", width=16, height=2, command=self.controller.start)
        self.btnRestart.pack(pady=10)

    def show_message(self, message):
        popup = tk.Toplevel()
        popup.title("Game Over")
        msg = tk.Label(popup, text=message, font=('Arial', 14))
        msg.pack(pady=10, padx=10)
        btnClose = tk.Button(popup, text="Close", command=popup.destroy)
        btnClose.pack(pady=5)

    def disable_input(self):
        self.entryLetter.config(state='disabled')
        self.btnCheck.config(state='disabled')

    def enable_input(self):
        self.entryLetter.config(state='normal')
        self.btnCheck.config(state='normal')

    def start(self):
        self.labelStage.config(text=self.stages[0])
        self.enable_input()
        self.root.mainloop()