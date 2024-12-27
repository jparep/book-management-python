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
            "is_borrowed": self.is_borrowed,
        }
        
    @staticmethod
    def from_dict(book_dict):
        """Creates a book object from a dictionary."""
        return Book(book_dict["book_id"], book_dict["title"], book_dict["author"], book_dict["is_borrowed"])
    
class Library:
    """"Mages a collection of books."""
    
    def __init__(self, file_name="books.json"):
        self.file_name = file_name
        self.books = []
        self.load_books()
    
    def load_books(self):
        """Loads the books from the json file."""
        try:
            with open(self.file_name, "r") as file:
                self.books = [Book.from_dict(book) for book in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = [] # If the file does not exist, create an empty list of books
        
    def save_books(self):
        """Saves the books to the json file."""
        with open(self.json_file_name, "w") as file:
            books = [book.to_dict() for book in self.books]
            json.dump(books, file)
    
    def add_book(self, book):
        """Adds a book to the library."""
        if any(b.book_id == book.book_id for b in self.books):
            print(f"Book with ID {book.book_id} already exists in the library.")
            return
        self.books.append(book)
        self.save_books()
        print(f"Book with ID {book.book_id} has been added to the library.")
        
    def display_books(self):
        """Displays the details of all the books in the library."""
        if not self.books:
            print("There are no books in the library.")
            return

        for book in self.books:
            book.display_book()
            
    def find_books(self, book_id):
        """"Find a books by its ID."""
        return next((book for book in self.books if book.book_id == book_id), None)
        
    def borrow_book(self, book_id):
        """Marks a book as borrowed of it is available."""
        book = self.find_book(book_id)
        if book:
            if book.is_borrowed:
                book.is_borrowed = True
                self.save_books()
                print(f"You have successfuly borrowed the book with title {book.title}.")
            else:
                print(f"Sorry, the book with title {book.title} is not available.")
        else:
            print(f"Sorry, the book with ID {book_id} is not available.")
    
    def return_book(self, book_id):
        """Returns a borrowed book to the library if it was borrowed."""
        book = self.find_books(book_id)
        if book:
            if book.is_borrowed:
                book.book_id = False
                self.save_books()
                print(f"You have successfuly returned the book with title {book.title}.")
            else:
                print(f"Sorry, the book with title {book.title} was not borrowed.")
        else:
            print(f"No book found with ID {book_id}.")
            
        
    def __del__(self):
        """Ensures that the books are saved when the library object is deleted."""
        self.save_books()
        
def main():
    library = Library()
    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a book to the library")
        print("2. Display all books in the library")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Book Author: ")
                library.add_book(Book(book_id, title, author))
            except ValueError:
                print("Invalid input. Book ID must be a number.")
                
        elif choice == "2":
            library.display_books()
            
        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID to borrow: "))
                library.borrow_book(book_id)
            except ValueError:
                print("Invalid input. Book ID must be a number.")
                
        elif choice == "4":
            try:
                book_id = int(input("Enter Book ID to return: "))
                library.return_book(book_id)
            except ValueError:
                print("Invalid input. Book ID must be a number.")
        elif choice == "5":
            
        elif choice == "5":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__=="__main__":
    main()