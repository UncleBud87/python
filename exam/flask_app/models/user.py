from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re # from pattern validation on learn platform

class User():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at'] # not actually needed unless its going to be called upon
        self.updated_at = data['updated_at'] # not actually needed unless its going to be called upon

    @classmethod
    def create_new_user(cls,data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'

        result = connectToMySQL('exam').query_db(query, data)

        return result

    @classmethod
    def get_user_by_email(cls,data):

        query = "SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL('exam').query_db(query, data)

        if len(results)  == 0:
            return False

        else:
            return User(results[0])

    @staticmethod
    def validate_new_user(data): # does not need class
        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        #first_name 3-50 characters
        if len(data['first_name']) < 3 or len(data ['first_name']) >50:
            is_valid = False
            flash('First name should be 3 to 50 characters long', 'register')

        if len(data['last_name']) < 3 or len(data ['last_name']) >50:
            is_valid = False
            flash('Last name should be 3 to 50 characters long', 'register')

        #email is not in use
        if User.get_user_by_email(data):
            is_valid = False
            flash('Email already in use', 'register')
        #email is valid
        if not email_regex.match(data['email']):
            is_valid = False
            flash('Email address not correctly formatted.', 'register')


        #password is of minimum length
        if len(data['password']) < 8:
            is_valid = False
            flash('Password should be atleast eight characters long.', 'register')
        #password and confirm password match
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash('Passwords do not match.', 'register')

        return is_valid