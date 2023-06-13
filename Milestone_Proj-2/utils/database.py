import sqlite3
from .database_connection import *

def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def db_add_book(name,author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try :
            cursor.execute('INSERT INTO books VALUES(?,?,0)' , (name,author))
        except sqlite3.IntegrityError: 
            print ('Book already exist!')
        except:
            print("chumma")
      


def db_list_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')

        books = [{'name': book[0] , 'author': book[1] , 'read': book[2] } for book in cursor.fetchall()]

    return books
            
def db_read_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name = ?',(name,))

def db_delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name = ?', (name,) )