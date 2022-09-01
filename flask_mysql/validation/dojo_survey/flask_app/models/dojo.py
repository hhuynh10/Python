from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    db = "dojo_survey_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls,data):
        query = """INSERT INTO dojos (name, location, language, comment)
        VALUES (%(name)s, %(location)s, %(language)s, %(comment)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def read(cls):
        query = """SELECT * FROM dojos
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
            return dojos
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 5:
            flash("Name must be at least 5 characters.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("Must choose one location.")
            is_valid = False
        if len(dojo['language']) < 1:
            flash("Must choose one language.")
            is_valid = False
        if len(dojo['comment']) < 50:
            flash("Comment must be at least 50 characters.")
            is_valid = False
        return is_valid