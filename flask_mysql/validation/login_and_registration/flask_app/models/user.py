from pickle import FALSE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.confirm_password = data['confirm_password']

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true

        if len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False
        if User.get_by_email(user) != False:
            flash('Email already in use', 'error')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password does not match.")
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user_registration WHERE email = %(email)s;"
        result = connectToMySQL('user_registration_schema').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user_registration (first_name,last_name,email,password,confirm_password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(confirm_password)s);"
        result = connectToMySQL('users_registration_schema').query_db(query,data)
        return result
