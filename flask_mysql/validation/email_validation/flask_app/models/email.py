from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    db = "email_schema"
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = """INSERT INTO emails (email, created_at)
        VALUES (%(email)s, NOW())
        ;"""
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def read(cls):
        query = """SELECT * FROM emails
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        emails = []
        for email in result:
            emails.append(cls(email))
        return emails

    @classmethod
    def delete(cls, data):
        query = """DELETE FROM emails
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.db).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid