import json
import os

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)  # Fixed incorrect function call
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)  # Added indent for readability

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read_status = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {  # Fixed indentation
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read_status': read_status
    }

    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added to the library...')

def remove_book(library):
    title = input('Enter the title of the book to remove from the library: ')
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title.lower()]
    
    if len(library) < initial_length:
        save_library(library)
        print(f'Book "{title}" removed from the library...')
    else:
        print(f'Book "{title}" does not exist in the library...')

def search_library(library):
    search_by = input('Search by title or author: ').strip().lower()
       # Validate input to ensure it's either 'title' or 'author'
    if search_by not in ["title", "author"]:
        print("Invalid search option. Please enter 'title' or 'author'.")
        return

    search_term = input(f'Enter the {search_by}: ').strip().lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            read_status = "Read" if book['read_status'] else "Not Read"
            print(f"Title: {book['title']}, Author: {book['author']} - {book['genre']} - {read_status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            read_status = "Read" if book['read_status'] else "Not Read"
            print(f"Title: {book['title']}, Author: {book['author']} - {book['year']} - {book['genre']} - {read_status}")
    else:
        print("No books in the library...")

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read_status']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    library = load_library()
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again...")

if __name__ == '__main__':
    main()








