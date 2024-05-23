class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_biography(self):
        return self.__biography

    def set_biography(self, value):
        self.__biography = value

    def __str__(self):
        return f"Author: {self.__name}\nBiography: {self.__biography}"