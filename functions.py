from book import Book
from user import User
from author import Author
from genre import Genre

def add_book(books):
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        genre = input("Enter book genre: ")
        publication_date = input("Enter book publication date (YYYY-MM-DD): ")
        book = Book(title, author, isbn, genre, publication_date)
        books.append(book)
        print("Book added successfully!")
    except Exception as e:
        print(f"Error adding book: {e}")

def borrow_book(books):
    try:
        isbn = input("Enter ISBN of the book to borrow: ")
        book = next((b for b in books if b.get_isbn() == isbn), None)
        if book and book.is_available():
            book.borrow()
            print(f"You have borrowed: {book.get_title()}")
        else:
            print("Book not found or already borrowed.")
    except Exception as e:
        print(f"Error borrowing book: {e}")

def return_book(books):
    try:
        isbn = input("Enter ISBN of the book to return: ")
        book = next((b for b in books if b.get_isbn() == isbn), None)
        if book and not book.is_available():
            book.return_book()
            print(f"You have returned: {book.get_title()}")
        else:
            print("Book not found or not borrowed.")
    except Exception as e:
        print(f"Error returning book: {e}")

def search_book(books):
    isbn = input("Enter ISBN of the book to search: ")
    book = next((b for b in books if b.get_isbn() == isbn), None)
    if book:
        print(book)
    else:
        print("Book not found.")

def display_books(books):
    for book in books:
        print(book)

def add_user(users):
    try:
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        user = User(name, library_id)
        users.append(user)
        print("User added successfully!")
    except Exception as e:
        print(f"Error adding user: {e}")

def view_user(users):
    library_id = input("Enter library ID of the user: ")
    user = next((u for u in users if u.get_library_id() == library_id), None)
    if user:
        print(user)
    else:
        print("User not found.")

def display_users(users):
    for user in users:
        print(user)

def add_author(authors):
    try:
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        author = Author(name, biography)
        authors.append(author)
        print("Author added successfully!")
    except Exception as e:
        print(f"Error adding author: {e}")

def view_author(authors):
    name = input("Enter name of the author: ")
    author = next((a for a in authors if a.get_name() == name), None)
    if author:
        print(author)
    else:
        print("Author not found.")

def display_authors(authors):
    for author in authors:
        print(author)

def add_genre(genres):
    try:
        name = input("Enter genre name: ")
        description = input("Enter genre description: ")
        category = input("Enter genre category: ")
        genre = Genre(name, description, category)
        genres.append(genre)
        print("Genre added successfully!")
    except Exception as e:
        print(f"Error adding genre: {e}")

def view_genre(genres):
    name = input("Enter name of the genre: ")
    genre = next((g for g in genres if g.get_name() == name), None)
    if genre:
        print(genre)
    else:
        print("Genre not found.")

def display_genres(genres):
    for genre in genres:
        print(genre)