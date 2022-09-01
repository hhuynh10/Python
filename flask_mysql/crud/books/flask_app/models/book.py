from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask_app.models import book

class Book:
    db = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.number_of_page = data['number_of_page']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
    
# CREATE BOOKS
    @classmethod
    def add_book(cls, data):
        query = """INSERT INTO books (title, number_of_page)
        VALUES (%(title)s, %(number_of_page)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

# READ AUTHOR
    @classmethod
    def read_books(cls):
        query= """SELECT *
        FROM books
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        books = []
        for book in result:
            books.append(cls(book))
        return books

    @classmethod
    def get_book_with_authors( cls , data ):
        query = """SELECT * FROM books 
        LEFT JOIN favorites ON favorites.book_id = books.id 
        LEFT JOIN authors ON favorites.author_id = authors.id 
        WHERE books.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db( query , data )
        book = cls( results[0] )
        for row_from_db in results:
            if row_from_db['authors.id'] == None:
                break
            author_data = {
                "id" : row_from_db["author.id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            book.authors.append( author.Author( author_data ) )
        return book
    
    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL(cls.db).query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books