from .database_connection import DatabaseConnectionClass

def create_book_table():
    with DatabaseConnectionClass('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)')


def add_book(name, author):
    with DatabaseConnectionClass('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO books VALUES (?, ?, 0)', (name, author))


def get_all_books():
    with DatabaseConnectionClass('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name' : row[0], 'author' : row[1], 'read' : row[2]} for row in cursor.fetchall()]
        return books


def mark_book_read(name):
    with DatabaseConnectionClass('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books set read = 1 where name = ?", (name,))


def delete_book(name):
    with DatabaseConnectionClass('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books where name = ?", (name,))