import json


class Book:
    """Represents a book with its details."""

    def __init__(self, book_id, title, author, is_borrowed=False):
        self.book_id = int(book_id)
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def display(self):
        """Displays the details of a book."""
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}")

    def to_dict(self):
        """Converts the book object to a dictionary."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed,
        }

    @staticmethod
    def from_dict(data):
        """Creates a book object from a dictionary."""
        return Book(data["book_id"], data["title"], data["author"], data["is_borrowed"])


class Library:
    """Manages a collection of books."""

    def __init__(self, file_name="books.json"):
        self.file_name = file_name
        self.books = []
        self.load_books()

    def load_books(self):
        """Loads books from the JSON file."""
        try:
            with open(self.file_name, "r") as file:
                self.books = [Book.from_dict(book) for book in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []  # If the file doesn't exist or is corrupted, start fresh

    def save_books(self):
        """Saves the current state of books to the JSON file."""
        with open(self.file_name, "w") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, book):
        """Adds a book to the library."""
        if any(b.book_id == book.book_id for b in self.books):
            print(f"A book with ID {book.book_id} already exists.")
            return
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' has been added to the library.")

    def display_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("No books are currently in the library.")
            return
        for book in self.books:
            book.display()

    def find_book(self, book_id):
        """Finds a book by its ID."""
        return next((book for book in self.books if book.book_id == book_id), None)

    def borrow_book(self, book_id):
        """Marks a book as borrowed if available."""
        book = self.find_book(book_id)
        if book:
            if not book.is_borrowed:
                book.is_borrowed = True
                self.save_books()
                print(f"You have successfully borrowed '{book.title}'.")
            else:
                print(f"The book '{book.title}' is already borrowed.")
        else:
            print(f"No book found with ID {book_id}.")

    def return_book(self, book_id):
        """Marks a book as returned if it was borrowed."""
        book = self.find_book(book_id)
        if book:
            if book.is_borrowed:
                book.is_borrowed = False
                self.save_books()
                print(f"You have successfully returned '{book.title}'.")
            else:
                print(f"The book '{book.title}' was not borrowed.")
        else:
            print(f"No book found with ID {book_id}.")

    def __del__(self):
        """Ensures books are saved when the library is destroyed."""
        self.save_books()


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Display All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
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
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
