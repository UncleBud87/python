from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models.user import User

import re

class Car():
    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.description = data['description']
        self.seller = data['seller']
        self.price = data['price']
        self.created_at = data['created_at'] # not actually needed unless its going to be called upon
        self.updated_at = data['updated_at'] # not actually needed unless its going to be called upon
        self.users_id = data['users_id']

    @classmethod
    def create_car(cls, data):

        query = 'INSERT INTO cars (make, model, price, year, description, users_id) VALUES (%(make)s, %(model)s, %(price)s, %(year)s, %(description)s, %(users_id)s);'

        result = connectToMySQL('exam').query_db(query,data)

        return result

    @classmethod
    def update_car(cls, data):

        query = 'UPDATE cars SET make = %(car_make)s, model = %(car_model)s, price = %(car_price)s, year = %(car_year)s, description = %(car_description)s WHERE id = %(car_id)s;'

        result = connectToMySQL('exam').query_db(query,data)

        return result

    @classmethod
    def get_all_cars(cls):

        query = 'SELECT * FROM cars JOIN users ON cars.users_id = users.id;'

        results = connectToMySQL('exam').query_db(query)

        cars = []

        for item in results:
            new_car = Car(item)

            user_data = {
                'id': item['users.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['created_at'],
                'updated_at': item['updated_at']
            }

            new_car.user = User(user_data)

            cars.append(new_car)

        return cars

    @classmethod
    def get_car_by_id(cls, data):

        query = 'SELECT * FROM cars JOIN users ON cars.users_id = users.id WHERE cars.id = %(id)s;'

        result = connectToMySQL('exam').query_db(query,data)

        car =  Car(result[0])

        user_data = {
                'id': result[0]['users.id'],
                'first_name': result[0]['first_name'],
                'last_name': result[0]['last_name'],
                'email': result[0]['email'],
                'password': result[0]['password'],
                'created_at': result[0]['created_at'],
                'updated_at': result[0]['updated_at']
            }

        car.user = User(user_data)

        return car

    @classmethod
    def delete_car(cls,data):
        query = 'DELETE FROM cars WHERE id = %(id)s;'

        result = connectToMySQL('exam').query_db(query,data)

    @staticmethod
    def validate_car(data):
        is_valid = True

        if len(data['car_make']) < 1 or len(data['car_make']) > 50:
            is_valid = False
            flash('Car make should be between 1 and 50 characters long', 'car')
        
        if len(data['car_model']) < 1 or len(data['car_model']) > 50:
            is_valid = False
            flash('Car model should be between 1 and 50 characters long', 'car')

        if len(data['car_description']) < 1 or len(data['car_description']) >250:
            is_valid = False
            flash('Car description should be between 1 and 250 characters long', 'car')

        if 'car_price' not in data:
            is_valid = False
            flash('Choose a price greater than 0', 'car')
        
        if 'car_year' not in data:
            is_valid = False
            flash('Choose a year greater than 0', 'car')


        return is_valid