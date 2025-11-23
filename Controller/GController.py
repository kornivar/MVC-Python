from View.GView import GView
from Model.GModel import GModel

class GController:
    def __init__(self):
        self.gview = GView(self)
        self.gmodel = GModel()

    def display_word(self):
        display = ''
        for letter in self.gmodel.letters:
            if letter in self.gmodel.guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        self.gview.labelWord.config(text=display.strip())

    def display_attempts(self):
        stage = self.gmodel.stage_count
        self.gview.labelAttempts.config(text=f"Attempts left: {6-stage}")

    def display_letter(self):
        letter = self.gview.entryLetter.get().lower()
        result = self.gmodel.check_letter(letter)

        if result is None:
            self.gview.show_message("You already tried this letter!")
            return

        self.display_word()
        self.display_attempts()

        self.gview.labelStage.config(text=self.gview.stages[self.gmodel.stage_count])
        if all(letter in self.gmodel.guessed_letters for letter in self.gmodel.letters):
            self.gview.show_message("Congratulations! You've won!")
            self.gview.disable_input()
        elif self.gmodel.stage_count >= 6:
            self.gview.show_message(f"You've lost! The word was: {self.gmodel.word}")
            self.gview.disable_input()

    def start(self):
        self.gmodel.get_word()
        self.gmodel.get_letters()
        self.display_word()
        self.display_attempts()
        self.gview.start()