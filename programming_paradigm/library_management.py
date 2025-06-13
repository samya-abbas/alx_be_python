class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return

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
                if book.check_out():
                    print(f"Book '{title}' has been checked out.")
                else:
                    print(f"Book '{title}' is already checked out.")
                return
        if not found:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.return_book():
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' was not checked out.")
                return
        if not found:
            print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        available_books_found = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_books_found = True
        if not available_books_found:
            print("No books are currently available.")
