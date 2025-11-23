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
        self.word = ""
        self.stage_count = 0
        self.letters = []
        self.guessed_letters = []

    def get_word(self):
        self.word = random.choice(self.words)
        self.letters = []
        self.guessed_letters = []
        self.stage_count = 0

    def get_letters(self):
        for i in self.word:
            self.letters.append(i)

    def check_letter(self, letter):
        if letter in self.guessed_letters:
            return None   

        if letter in self.letters:
            self.guessed_letters.append(letter)
            return True

        self.stage_count += 1
        return False
        

