from Controller.NoteController import NoteController
from Model.Note import Note


class ConsoleView:
    def __init__(self):
        self.__noteController = NoteController()

    def showAll(self):
        for elem in self.__noteController.getAll():
            print(f"{elem.title}\n{elem.text}\n")
    def add(self):
        print("Enter title ")
        title = input()
        print("Enter text ")
        text = input()

        newNote = Note(title, text)

        self.__noteController.add(newNote)

    def find(self, value):
        notes = self.__noteController.getAll()
        flag = False
        for obj in notes:
            if value.lower() in obj.title.lower():
                print("Note found!")
                print(f"Title: {obj.title}")
                print(f"Text: {obj.text}")
                flag = True
        if not flag:
            print("No such note")