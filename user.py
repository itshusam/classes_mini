class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, value):
        self.__library_id = value

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        self.__borrowed_books.remove(book)

    def __str__(self):
        return f"User: {self.__name} (ID: {self.__library_id})"