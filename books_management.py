# Import libaries
import json

class Book:
    """Initializes a books with its details."""
    def __init__(self, book_id, title, author, is_borrowed=False):
        self.book_id = int(book_id)
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def display(self):
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
    def __init__(self, json_file_name="books.json"):
        self.json_file_name = json_file_name
        self.books = []
        self.load_books()
    
    def load_books(self):
        """Loads the books from the json file."""
        try:
            with open(self.json_file_name, "r") as file:
                books = json.load(file)
                for book in books:
                    self.books.append(Book.from_dict(book))
        except FileNotFoundError:
            self.books = [] # If the file does not exist, create an empty list of books
        
    def save_books(self):
        """Saves the books to the json file."""
        with open(self.json_file_name, "w") as file:
            books = [book.to_dict() for book in self.books]
            json.dump(books, file)
    
    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)
        self.save_books()
        print(f"Book with ID {book.book_id} has been added to the library.")
        
    def display_books(self):
        """Displays the details of all the books in the library."""
        if len(self.books) == 0:
            print("There are no books in the library.")
            return
        elif not self.books:
            print("There is no books in the library.")
            return
        else:
            for book in self.books:
                book.display_book()
        
    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed the book with ID {book_id}.")
                else:
                    print(f"Sorry, the book with ID {book_id} is already borrowed.")
                return
        print(f"Sorry, the book with ID {book_id} is not available.")
    
    def return_book(self, book_id):
        """Returns a borrowed book to the library."""
        for book in self.books:
            if book.book_id  == book_id:
                if book.is_borrowed:
                    book.is_boorrowed = False
                    print(f"You have returned the book with ID {book_id}.")
                else:
                    print(f"Sorry, the book with ID {book_id} was not borrowed.")
        print(f"Sorry, the book with ID {book_id} is not available.")
        
    def __del__(self):
        """Ensures that the books are saved when the library object is deleted."""
        self.save_books()
        
def main():
    libray = Library()
    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a book to the library")
        print("2. Display all books in the library")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_id = input("Enter the book ID:")
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            libray.add_book(Book(book_id, title, author))
        elif choice == "2":
            libray.display_books()
        elif choice == "3":
            book_id = input("Enter the book ID to borrow: ")
            libray.borrow_book(book_id)
        elif choice == "4":
            book_id = input("Enter the book ID to return: ")
            libray.return_book(book_id)
        elif choice == "5":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()