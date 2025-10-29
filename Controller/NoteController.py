class  NoteController:
    def __init__(self):
        self.__notes = []

    def add(self, note):
        self.__notes.append(note)
    def delete(self, note):
        self.__notes.remove(note)

    def getAll(self):
        return self.__notes