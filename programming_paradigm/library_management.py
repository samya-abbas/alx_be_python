class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book (public).
        author (str): The author of the book (public).
        _is_checked_out (bool): Private attribute to track if the book is checked out.
                                 True if checked out, False otherwise.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # By default, a new book is not checked out

class Library:
    """
    Manages a collection of books.

    Attributes:
        _books (list): A private list to store Book instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
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
        """
        Marks a book as checked out if it is available.

        Args:
            title (str): The title of the book to check out.
        """
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
        """
        Marks a book as returned if it was checked out.

        Args:
            title (str): The title of the book to return.
        """
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
        """
        Prints the title and author of all books that are currently not checked out.
        If no books are available, it prints a message indicating so.
        """
        available_books_found = False
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
                available_books_found = True
        if not available_books_found:
            print("No books are currently available.")


