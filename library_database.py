# This module acts as our simple library database.
# We use basic Python lists to hold all the book records.

# ---BOOK RECORD LIST ---
# Structure: [Title, Author, Status (Available/Checked Out)]
BOOK_LIST = [
    ["The Great Gatsby", "F. Scott Fitzgerald", "Available"],
    ["1984", "George Orwell", "Available"],
    ["To Kill a Mockingbird", "Harper Lee", "Available"],
    ["Moby Dick", "Herman Melville", "Available"],
    ["Pride and Prejudice", "Jane Austen", "Available"]
]

def get_all_books():
    #Returns the complete list of all books and their details.
    return BOOK_LIST

def get_book_status(index):
    """Retrieves the current status (Available/Checked Out) of a book by its number."""
    try:
        return BOOK_LIST[index][2]
    except IndexError:
        return "ERROR: Book not found"

def update_book_status(index, new_status):
    """Changes the status of a book.
    Returns True if successful, False if the index is wrong.
    """
    try:
        BOOK_LIST[index][2] = new_status
        return True
    except IndexError:
        return False

def get_book_details(index):
    """Retrieves the Title and Author of a book."""
    try:
        return BOOK_LIST[index][0], BOOK_LIST[index][1] 
    except IndexError:
        return "Unknown Book", "Unknown Author"
        
def add_new_book(title, author):
    """
    Adds a new book record to the list. New books always start as 'Available'.
    """
    new_book = [title, author, "Available"]
    BOOK_LIST.append(new_book)
    return len(BOOK_LIST) - 1