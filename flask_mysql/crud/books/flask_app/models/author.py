from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


class Author:
    db = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
    
# CREATE AUTHOR
    @classmethod
    def add_author(cls, data):
        query = """INSERT INTO authors (name)
        VALUES (%(name)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

# READ AUTHOR
    @classmethod
    def read_authors(cls):
        query= """SELECT *
        FROM authors
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in result:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def get_author_with_books( cls , data ):
        query = """SELECT * FROM authors 
        LEFT JOIN favorites ON favorites.author_id = authors.id 
        LEFT JOIN books ON favorites.book_id = books.id 
        WHERE authors.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db( query , data )
        author = cls( results[0] )
        for row_from_db in results:
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "number_of_page" : row_from_db["number_of_page"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            author.books.append( book.Book( book_data ) )
        return author
    
    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL(cls.db).query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors
    
    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)