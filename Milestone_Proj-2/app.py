#Book Store Project
"""
Create a console-based book store system that allows users to:
Like the previous project, we'll use an in-memory database (i.e. a Python list,
which we're calling a database because it stores data).
 - Enter and retrieve book details.

 - Mark books as read (meaning they've finished reading them).

 - Delete existing books
 """
#from utils import database_like_file
#from utils.database_like_file import *

from utils.database import create_book_table, db_add_book, db_list_books, db_read_book, db_delete_book

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark books as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""

def menu():
    create_book_table()
    
    user_input = input(USER_CHOICE)

    while user_input.lower() != 'q':
        if user_input.lower() == 'a':
            add_book()

        elif user_input.lower() == 'l':
            list_books()

        elif user_input.lower() == 'r':
            read_book()

        elif user_input.lower() == 'd':
            delete_book()

        else:
            print('Unknown Command. Try again!')

        user_input = input(USER_CHOICE)

#add_book
def add_book():
    name = input('Enter book name: ')
    author = input('Enter author name: ')
    db_add_book(name,author)

def list_books():
    contents = db_list_books()
    print(contents)

def read_book():
    name = input('Enter book name which you have read: ')
    db_read_book(name)
     
def delete_book():
    name = input('Enter the book which need to be deleted: ')
    db_delete_book(name)
     
# call main function       
menu()