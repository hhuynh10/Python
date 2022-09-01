from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    db = 'dojos_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

#CREATE DOJO
    @classmethod
    def create_dojo(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at)
        VALUES (%(name)s, NOW(), NOW())
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)


#READ DOJO
    @classmethod
    def read_dojo(cls):
        query = """SELECT * 
        FROM dojos
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """SELECT * FROM dojos 
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        dojo = cls(results[0])
        for row_db in results:
            ninja_data = {
                "id" : row_db['ninjas.id'],
                "first_name" : row_db['first_name'],
                "last_name" : row_db['last_name'],
                "age" : row_db['age'],
                "created_at" : row_db['ninjas.created_at'],
                "updated_at" : row_db['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo


#DELETE DOJO
    @classmethod
    def delete_dojo(cls, data):
        query = """DELETE FROM dojos
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query,data)
