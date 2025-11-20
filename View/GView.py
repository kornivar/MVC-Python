import tkinter as tk

class GView:
    def __init__(self):
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

        labelG = tk.Label(self.root, text=self.stages[3], font=('Courier', 14), bg = "lightblue", justify="left")
        labelG.pack(pady=10, anchor="n", padx=50)

        labelW = tk.Label(self.root, text="Enter day", font=('Arial', 14), bg = "lightblue")
        labelW.pack()


    def on_button_click(self):
        self.controller.handle_button_click()

    def update_label(self, new_text):
        self.label.config(text=new_text)

    def start(self):
        self.root.mainloop()