# Library Management System

## Overview
The Library Management System is a Python-based application that allows users to manage a collection of books. It provides functionalities to add, display, borrow, and return books. The system uses a JSON file for data persistence, ensuring that all book details are saved between sessions.

---

## Features
1. **Add Book**: Add a new book to the library with a unique ID, title, and author.
2. **Display Books**: View all books in the library with their status (Available or Borrowed).
3. **Borrow Book**: Mark a book as borrowed if it is available.
4. **Return Book**: Mark a borrowed book as returned.
5. **Persistent Storage**: Books are stored in a `books.json` file, ensuring data is not lost when the application closes.

---

## Technologies Used
- **Python**: Core programming language.
- **JSON**: Used for data storage and retrieval.

---

## Installation and Setup
### Prerequisites
- Python 3.7+

### Steps
1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/book-management-python.git
   cd book-management-python
   ```

2. Ensure Python is installed on your machine. Verify with:
   ```bash
   python --version
   ```

3. Run the application:
   ```bash
   python book_management.py
   ```

---

## Usage
Upon running the application, you will see a menu with the following options:

```
Library Management System
1. Add a Book
2. Display All Books
3. Borrow a Book
4. Return a Book
5. Exit
```

### Example Walkthrough
#### 1. Add a Book
```
Enter Book ID: 1
Enter Book Title: 1984
Enter Book Author: George Orwell
Book '1984' has been added to the library.
```

#### 2. Display All Books
```
ID: 1 | Title: 1984 | Author: George Orwell | Status: Available
```

#### 3. Borrow a Book
```
Enter Book ID to borrow: 1
You have successfully borrowed '1984'.
```

#### 4. Return a Book
```
Enter Book ID to return: 1
You have successfully returned '1984'.
```

---

## File Structure
```
.
├── library_system.py       # Main application script
├── books.json              # Data file for storing book information
└── README.md               # Documentation for the project
```

---

## Future Enhancements
- Add user management for tracking who borrows each book.
- Implement a graphical user interface (GUI).
- Integrate with a database (e.g., SQLite or MongoDB) for large-scale usage.
- Enable search and filter functionality for books.

---

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

## Contact
For questions or contributions, feel free to contact:
- **Email**: contact@joshuaparep.com
- **GitHub**: [https://github.com/jparep](https://github.com/jparep)
