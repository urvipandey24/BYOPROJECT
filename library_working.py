# This module handles the rules for checking books in and out, and adding new records.
# It uses functions from library_data to read and write the status.

from library_database import get_book_status, update_book_status, get_all_books, add_new_book

def check_out_book(index):
    """
    Attempts to change a book's status from 'Available' to 'Checked Out'.
    """
    current_status = get_book_status(index)
    
    if current_status == "Available":
        if update_book_status(index, "Checked Out"):
            return "SUCCESS: Book successfully checked out."
        else:
            return "ERROR: Problem updating the book status."
    
    elif current_status == "Checked Out":
        return "FAIL: That book is currently out."
        
    else:
        return "ERROR: Invalid book number."


def return_book(index):
    """
    Attempts to change a book's status from 'Checked Out' back to 'Available'.
    """
    current_status = get_book_status(index)
    
    if current_status == "Checked Out":
        if update_book_status(index, "Available"):
            return "SUCCESS: Book successfully returned to the shelf."
        else:
            return "ERROR: Problem updating the book status."
            
    elif current_status == "Available":
        return "FAIL: That book was already here!"
        
    else:
        return "ERROR: Invalid book number."

def register_new_book(title, author):
    """
    Uses the data module to add a new book based on user provided input.
    """
    new_index = add_new_book(title, author)
    return new_index

def count_available_books():
    """Counts how many books are currently available in the list."""
    
    books = get_all_books()
    count = 0
    
    # Simple loop to check the status of every book
    for book in books:
        # We know the status is at index 2
        if book[2] == "Available":
            count += 1
            
    return count