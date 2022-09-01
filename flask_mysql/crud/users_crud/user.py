from mysqlconnection import connectToMySQL

class User:
    db = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']

# CREATE
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

#READ
    @classmethod
    def read_user(cls):
        query= """SELECT *
        FROM users
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users
    
    @classmethod
    def read_one(cls, data):
        query = """SELECT *
        FROM users
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])



#UPDATE
    @classmethod
    def update_user(cls, data):
        query = """UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

#DELETE
    @classmethod
    def delete_user(cls, data):
        query = """DELETE FROM users
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)
