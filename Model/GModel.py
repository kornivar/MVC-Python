import random
class GModel:
    def __init__(self):
        self.words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
        self.word = self.get_word()
        self.letters = []
        self.guessed_letters = []

    def get_word(self):
        return random.choice(self.words)

    def get_letters(self):
        for i in self.word:
            self.letters.append(i)

    def check_letter(self, letter):
        return letter in self.letters

