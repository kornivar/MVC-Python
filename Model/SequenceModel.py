class SequenceModel:
    def __init__(self, seq):
        self.__seq = seq

    @property
    def seq(self):
        return self.__seq

    @seq.setter
    def seq(self, value):
        self.__seq = value