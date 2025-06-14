class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # By default, a new book is not checked out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return

        # Check if a book with the same title and author already exists
        for existing_book in self._books:
            if existing_book.title == book.title and existing_book.author == book.author:
                print(f"Book '{book.title}' by {book.author} already exists in the library.")
                return

        self._books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def check_out_book(self, title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"Book '{title}' has been checked out.")
                else:
                    print(f"Book '{title}' is already checked out.")
                return # Exit once the book is found and processed
        if not found:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' was not checked out.")
                return # Exit once the book is found and processed
        if not found:
            print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        available_books_found = False
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
                available_books_found = True
        if not available_books_found:
            print("No books are currently available.")
