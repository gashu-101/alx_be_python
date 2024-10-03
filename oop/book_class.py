class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String Representation: Returns a string describing the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official Representation: Returns a string to recreate the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
