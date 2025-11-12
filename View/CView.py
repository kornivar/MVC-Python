import tkinter as tk

class CView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x275")
        self.root.title("Calculator")

    def on_button_click(self):
        self.controller.handle_button_click()

    def update_label(self, new_text):
        self.label.config(text=new_text)

    def start(self):
        self.root.mainloop()