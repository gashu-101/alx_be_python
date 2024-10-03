# Base class Book
class Book:
    def __init__(self, title: str, author: str):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

# Derived class EBook inheriting from Book
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class PrintBook inheriting from Book
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class for managing a collection of books (composition)
class Library:
    def __init__(self):
        """Initialize a library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
