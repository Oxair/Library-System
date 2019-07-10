import sqlite3

class DatabaseConnectionClass:
    def __init__(self, host):
        self.connection = None
        self.host = host


    def __enter__(self):
        self.connection = sqlite3.connect('data.db')
        return self.connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()