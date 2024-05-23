class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    def get_category(self):
        return self.__category

    def set_category(self, value):
        self.__category = value

    def __str__(self):
        return f"Genre: {self.__name}\nDescription: {self.__description}\nCategory: {self.__category}"