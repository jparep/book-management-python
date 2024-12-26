# Import libaries
import json

class Book:
    """Initializes a books with its details."""
    def __init__(self, book_id, title, author, is_borrowed):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed