
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

        self.account = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user_registration (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s;"
        return connectToMySQL('login_registration').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "select * FROM user_registration WHERE id = %(id)s"
        return connectToMySQL('login_registration').query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user_registration WHERE email = %(email)s;"
        result = connectToMySQL('login_registration').query_db(query,data)

        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_account(account):
        is_valid = True
        if len(account['first_name']) < 2:
            flash("First Name must be atleast 2 characters", 'error')
            is_valid = False
        if len(account['last_name']) < 2:
            flash("Last Name must be atleast 2 characters", 'error')
            is_valid = False
        if not EMAIL_REGEX.match(account['email']):
            flash('Invalid email address!', 'error')
            is_valid = False
        if Regisrtr.get_by_email(account) != False :
            flash('Email already in use', 'error')
            is_valid = False
        if not PASSWORD_REGEX.match(account['password']):
            flash('Password cannot be empty and needs atleast one uppercase letter, one lowercase letter, and one number(MIN of 8 characters ) ', 'error')
            is_valid = False
        if account['password'] != account['confirm_password']:
            flash("Passwords do not match!", 'error')
            is_valid = False
        

        return is_valid

