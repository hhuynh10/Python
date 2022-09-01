from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash, session

class Report:
    db = 'reports'
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date = data['date']
        self.num = data['num']
        self.user_id = data['user_id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.users = None
    
# CREATE SQL
    @classmethod
    def create_report(cls,data):
        if not cls.validate_rep_data(data):
            return False
        query = """
        INSERT INTO reports (location, description, date, num, user_id)
        VALUES (%(location)s, %(description)s, %(date)s, %(num)s, %(user_id)s)
        ;"""
        report_id = connectToMySQL(cls.db).query_db(query, data)
        return report_id

# READ SQL
    @classmethod
    def view_all_reports(cls):
        query = """SELECT * FROM reports
        LEFT JOIN users
        ON reports.user_id = users.id
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        all_reports = []
        if not result:
            return result
        for this_report in result:
            new_report = cls(this_report)
            this_rep = {
                'id' : this_report['users.id'],
                'first_name' : this_report['first_name'],
                'last_name' : this_report['last_name'],
                'email' : this_report['email'],
                'password' : this_report['password'],
                'confirm_password' : this_report['confirm_password'],
                'created_at' : this_report['users.created_at'],
                'updated_at' : this_report['users.updated_at']
            }
            new_report.users = user.User(this_rep)
            all_reports.append(new_report)
        return all_reports
    
    @classmethod
    def view_one_report(cls, id):
        data = {'id' : id}
        query = """SELECT *
        FROM reports
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result

# UPDATE SQL
    @classmethod
    def update_report(cls, id):
        query = """UPDATE reports
        SET location = %(location)s, description = %(description)s, date = %(date)s, num = %(num)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, id)

# DELETE SQL
    @classmethod
    def delete_report(cls, id):
        data = {'id' : id}
        query = """DELETE FROM reports
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)

# VALIDATE SQL
    @staticmethod
    def validate_rep_data(data):
        is_valid = True
        if len(data['location']) < 2:
            flash ('Location must be at least 2 characters long.')
            is_valid = False
        if len(data['description']) < 10:
            flash ('Description must be at least 10 characters long.')
            is_valid = False
        if data['date'] == "":
            is_valid = False
            flash("Please enter a date")
        if len(data['num']) < 1:
            flash ('Number must be at least 1.')
        return is_valid