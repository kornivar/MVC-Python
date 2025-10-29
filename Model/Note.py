class Note:
    def __init__(self, title, text):
        self.__title = title
        self.__text = text

    @property
    def title(self):
        return self.__title
    @property
    def text(self):
        return self.__text

    @title.setter
    def title(self, value):
        self.__title = value
    @text.setter
    def text(self, value):
        self.__text = value