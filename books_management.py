# Import libaries
import json

class Book:
    """Initializes a books with its details."""
    def __init__(self, book_id, title, author, is_borrowed):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def displayBook(self):
        """Displays the details of a book."""
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}")
        
    def to_dict(self):
        """Converts the book details to a dictionary."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }
        
    @staticmethod
    def from_dict(book_dict):
        """Creates a book object from a dictionary."""
        return Book(book_dict["book_id"], book_dict["title"], book_dict["author"], book_dict["is_borrowed"])
    
class Library:
    def __init__(self):
        pass 
        