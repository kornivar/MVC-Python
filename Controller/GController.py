from View.GView import GView
from Model.GModel import GModel

class GController:
    def __init__(self):
        self.gview = GView(self)
        self.gmodel = GModel()

    def display_word(self):
        self.gmodel.get_letters()
        display = ''
        for letter in self.gmodel.letters:
            if letter in self.gmodel.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        self.gview.labelWord.config(text=display.strip())

    def start(self):
        self.display_word()
        self.gview.start()