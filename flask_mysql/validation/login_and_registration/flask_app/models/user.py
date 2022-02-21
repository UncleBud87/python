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

        if len(user['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 8:
            flash("email must me longer than 8 characters.")
            is_valid = False
        if len(user['password']) != len(user['confirm_password']):
            flash("Password does not match.")
            is_valid = False
        return is_valid