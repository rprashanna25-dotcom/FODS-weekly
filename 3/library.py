"""
this program builds a simple library system
it lets users search, borrow, and return books
book information is saved in a file
it applies object oriented programming concepts
it also handles errors using try except
"""

import csv

class Book:
    """
    class used to represent a book
    """

    def __init__(self, book_id, title, author, status="available"):
        """
            set initial values for book attributes
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        
    def list(self):
        """
        convert book object into list format for saving

        """
        return [self.book_id, self.title, self.author, self.status]


class Library:
    """
    class responsible for handling library functions

    """
    def __init__(self, file_name):
        """
        initialize library with a file name

        """
        self.file_name = file_name
    def load_book_list(self):
        """
        retrieve books from the file

        """
        books = []
        try:
            with open(self.file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    books.append(Book(row[0], row[1], row[2], row[3]))
        except FileNotFoundError:
            pass
        return books
    def store_books(self, books):
        """
        store books into the file
        """
        try:
            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                for book in books:
                    writer.writerow(book.list())
        except Exception:
            print("error while saving books")

    def find_book(self, keyword):
        """
        find a book using title keyword
        """
        books = self.load_book_list()
        found = False
        for book in books:
            if keyword.lower() in book.title.lower():
                print(f"{book.book_id} | {book.title} | {book.author} | {book.status}")
                found = True
        if not found:
            print("no book found")

    def mark_book_borrowed(self, book_id):
        """
        allow borrowing of a book if it is available

        """
        books = self.load_book_list()
        for book in books:
            if book.book_id == book_id:
                if book.status == "available":
                    book.status = "borrowed"
                    self.store_books(books)
                    print("book borrowed successfully")
                    return
                else:
                    print("book already borrowed")
                    return
        print("book not found")

    def mark_book_returned(self, book_id):
        """
        handle returning of a borrowed book

        """
        books = self.load_book_list()
        for book in books:
            if book.book_id == book_id:
                if book.status == "borrowed":
                    book.status = "available"
                    self.store_books(books)
                    print("book returned successfully")
                    return
                else:
                    print("book was not borrowed")
                    return
        print("book not found")


# create library object
library = Library("books.csv")

# sample initial data if file is empty
try:
    open("books.csv", "x").close()
    library.store_books([
        Book("1", "Eat that Frog", "Brian Tracy"),
        Book("2", "Think and grow rich", "Napolean Hill"),
        Book("3", "You can Win", "Shiv Khera")
    ])
except FileExistsError:
    pass


# main menu loop
while True:
    print("\n1 search book")
    print("2 borrow book")
    print("3 return book")
    print("4 exit")

    choice = input("enter choice: ")

    if choice == "1":
        keyword = input("enter book title to search: ")
        library.find_book(keyword)
    elif choice == "2":
        book_id = input("enter book id to borrow: ")
        library.mark_book_borrowed(book_id)
    elif choice == "3":
        book_id = input("enter book id to return: ")
        library.mark_book_returned(book_id)
    elif choice == "4":
        break
    else:
        print("invalid choice")