class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def set_title(self, value):
        self.__title = value

    def get_author(self):
        return self.__author

    def set_author(self, value):
        self.__author = value

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, value):
        self.__isbn = value

    def get_genre(self):
        return self.__genre

    def set_genre(self, value):
        self.__genre = value

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, value):
        self.__publication_date = value

    def is_available(self):
        return self.__is_available

    def set_is_available(self, value):
        self.__is_available = value

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
        else:
            raise Exception("Book is already borrowed")

    def return_book(self):
        self.__is_available = True

    def __str__(self):
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn}) - {'Available' if self.__is_available else 'Borrowed'}"


    
class FictionBook(Book):
    def __init__(self, title, author, isbn, genre, publication_date, sub_genre):
        super().__init__(title, author, isbn, genre, publication_date)
        self.__sub_genre = sub_genre

    def get_sub_genre(self):
        return self.__sub_genre

    def set_sub_genre(self, value):
        self.__sub_genre = value

    def __str__(self):
        return super().__str__() + f" [Fiction - {self.__sub_genre}]"