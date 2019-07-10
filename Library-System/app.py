from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice is: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE).lower()
    while user_input != "q":
        if user_input == "a":
            add_book()
        elif user_input == "l":
            list_book()
        elif user_input == "r":
            read_book()
        elif user_input == "d":
            delete_book()
        else:
            print("Command unknown!")
        user_input = input(USER_CHOICE).lower()


def add_book():
    name = input("Enter the book name: ")
    author = input("Enter the author name: ")
    database.add_book(name, author)


def list_book():
    books = database.get_all_books()
    for book in books:
        read = "Yes" if book['read'] else "No"
        print(f"{book['name']} by {book['author']}\nRead: {read}")


def read_book():
    name = input("Enter the name of the book: ")
    database.mark_book_read(name)


def delete_book():
    name = input("Enter the name of the book to delete:")
    database.delete_book(name)

menu()