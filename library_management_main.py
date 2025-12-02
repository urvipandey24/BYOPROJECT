# This module is the main program interface the user interacts with.
from library_database import get_all_books, get_book_details
from library_working import check_out_book, return_book, count_available_books, register_new_book

def display_library_status():
    """Prints the full list of books and their statuses."""
    
    books = get_all_books()
    
    print("\n" + "="*70)
    print("      📚 LIBRARY CATALOG STATUS 📚")
    print("="*70)
    # Print the column headers
    print(f"{'No.':<5}{'Title':<30}{'Author':<20}{'Status':<15}")
    print("-" * 70)
    
    # Print each book's details
    for index, book in enumerate(books):
        title = book[0]
        author = book[1]
        status = book[2]
        print(f"{index:<5}{title:<30}{author:<20}{status:<15}")
        
    print("="*70 + "\n")
    print("Total Books Available:" ,count_available_books())


def get_user_index(prompt):
    """Safely asks the user for a book number (index)."""
    
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input.lower() == 'menu':
                return -1 
            
            index = int(user_input)
            
            # Simple check to make sure the number is in the valid range
            if 0 <= index < len(get_all_books()):
                return index
            else:
                print("That number is outside the list. Choose a number between" ,0, "and" ,len(get_all_books()) - 1)
        except ValueError:
            print(" Please enter a whole number, like 1 or 2, or type 'menu'.")

def handle_transaction(action_type):
    """Generic handler for check out and return transactions."""
    
    display_library_status()
    print(f"--- {action_type.capitalize()} Book ---")
    
    prompt = f"Enter the number of the book to {action_type} (or 'menu'): "
    book_index = get_user_index(prompt)
    
    if book_index == -1:
        return
        
    # Choose the correct logic function based on the action_type
    if action_type == 'check out':
        result = check_out_book(book_index)
    else: # 'return'
        result = return_book(book_index)
        
    print(f"\n[Result] {result}")
    
    # Print confirmation if the transaction was a success
    if "SUCCESS" in result:
        title, author = get_book_details(book_index)
        print(f"Transaction successful for: '{title}' by {author}.")

def handle_add_new_book():
    """
    Takes user input for the new book's details and adds it to the database.
    """
    print("\n--- 📝 ADD NEW BOOK TO CATALOG ---")
    
    # Taking user input for book details
    title = input("Enter the Title of the new book: ").strip()
    author = input("Enter the Author of the new book: ").strip()
    
    if not title or not author:
        print("❌ Title and Author cannot be empty. Book addition cancelled.")
        return
        
    # Call the logic function to register the new book
    new_index = register_new_book(title, author)
    
    print("\n✅ SUCCESS: Book Added!")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Catalog Number: {new_index}")


def show_main_menu():
    """Displays the main options to the user."""
    print("\n" + "="*40)
    print("      🏛 SIMPLE LIBRARY SYSTEM 🏛      ")
    print("="*40)
    print("1. View Full Catalog Status")
    print("2. Check Out a Book")
    print("3. Return a Book")
    print("4. Add New Book")
    print("5. Exit System")
    print("="*40)

def main():
    """
    The main program function. It contains the primary loop and handles
    user input to navigate the library system.
    """
    
    while True:
        show_main_menu()
        # This is the main user input for the application flow
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            display_library_status()
        elif choice == '2':
            handle_transaction('check out')
        elif choice == '3':
            handle_transaction('return')
        elif choice == '4':
            handle_add_new_book() 
        elif choice == '5':
            print("\nThank you for managing your library! Goodbye.")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")
            
# Start the application by calling the main function
main()