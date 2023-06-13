import json
import csv

books_txt = 'c:/Users/rajir/Python/Udemy/Python sample programs/Milestone_Proj-2/book_list.txt'
books = []

def create_book_table_file():
      with open(books_txt,'a'):
            pass

def db_add_book_file(name,author):
        with open(books_txt,'a') as file:
              file.write(f"{name},{author},0 \n")
        

def db_list_books_file():
        with open(books_txt,'r') as file:
            lines = [line.strip().split(',') for line in file.readlines()]
            return [
                  {'name': line[0], 'author': line[1], 'read': line[2] }
                  for line in lines
            ] 
            
def db_read_book_file(name):
        books = db_list_books()
        for book in books:
            if book['name'] == name:
                book['read'] = '1'
        _save_all_books_file(books)

def _save_all_books_file(books):
      with open(books_txt,'w') as file:
            for book in books:
                  file.write(f"{book['name']},{book['author']},{book['read']}\n")

def db_delete_book_file(name):
        books = db_list_books_file()
        books = [book for book in books if book['name'] != name]
        _save_all_books_file(books)


        """Alternate way
        global books
        books = [book for book in books if book['name'] != name]
        """


