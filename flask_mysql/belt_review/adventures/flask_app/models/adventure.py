from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash, session

class Adventure:
    db = 'adventures'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.place = data['place']
        self.date = data['date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.users = None
    
    
    @classmethod
    def create_adventure(cls,data):
        if not cls.validate_reg_data(data):
            return False
        query = """
        INSERT INTO adventures (title, place, date, description, user_id)
        VALUES (%(title)s, %(place)s, %(date)s, %(description)s, %(user_id)s)
        ;"""
        adventure_id = connectToMySQL(cls.db).query_db(query, data)
        return adventure_id
    
    @classmethod
    def view_all_adventures(cls):
        query = """SELECT * FROM adventures
        LEFT JOIN users
        ON adventures.user_id = users.id
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        all_adventures = []
        if not result:
            return result
        for this_adventure in result:
            new_adventure = cls(this_adventure)
            this_adventurer = {
                'id' : this_adventure['users.id'],
                'first_name' : this_adventure['first_name'],
                'last_name' : this_adventure['last_name'],
                'email' : this_adventure['email'],
                'password' : this_adventure['password'],
                'confirm_password' : this_adventure['confirm_password'],
                'created_at' : this_adventure['users.created_at'],
                'updated_at' : this_adventure['users.updated_at'],
            }
            new_adventure.users = user.User(this_adventurer)
            all_adventures.append(new_adventure)
        return all_adventures
    
    @classmethod
    def view_one_adventure(cls, id):
        data = {'id' : id}
        query = """SELECT *
        FROM adventures
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update_adventure(cls, data):
        query = """UPDATE adventures
        SET title = %(title)s, place = %(place)s, date = %(date)s, description = %(description)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_adventure(cls, id):
        data = {'id' : id}
        query = """DELETE FROM adventures
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_reg_data(data):
        is_valid = True
        if len(data['title']) < 5:
            flash ('Title must be at least 5 characters long.')
            is_valid = False
        if len(data['place']) < 2:
            flash ('Place must be at least 3 characters long.')
            is_valid = False
        if data['date'] == "":
            is_valid = False
            flash("Please enter a date")
        if len(data['description']) < 10:
            flash ('Desciption must be at least 10 characters long.')
            is_valid = False
        return is_valid