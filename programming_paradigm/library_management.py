# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book to the library by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
