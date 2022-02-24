from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models.user import User

import re





class Recipe():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_min = data['under_30_min']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def create_recipe(cls, data):

        query = 'INSERT INTO recipes (name, description, instructions, under_30_min, date_made, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30_min)s, %(date_made)s, %(user_id)s);'

        result = connectToMySQL('recipes_schema').query_db(query,data)

        return result

    @classmethod
    def get_all_recipes(cls):

        query = 'SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;'

        results = connectToMySQL('recipes_schema').query_db(query)

        recipes = []

        for item in results:
            new_recipe = Recipe(item)

            user_data = {
                'id': item['users.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['created_at'],
                'updated_at': item['updated_at']
            }

            new_recipe.user = User(user_data)

            recipes.append(new_recipe)

        return recipes

    @staticmethod
    def validate_new_recipe(data):
        is_valid = True

        if len(data['recipe_name']) < 1 or len(data['recipe_name']) >100:
            is_valid = False
            flash('Recipe name should be between 1 and 100 characters long', 'recipe')
        
        if len(data['recipe_description']) < 1 or len(data['recipe_description']) >250:
            is_valid = False
            flash('Recipe description should be between 1 and 250 characters long', 'recipe')

        if len(data['recipe_instructions']) < 1 or len(data['recipe_instructions']) >500:
            is_valid = False
            flash('Recipe instructions should be between 1 and 500 characters long', 'recipe')

        if len(data['recipe_date_made']) == '':
            is_valid = False
            flash('Date made is required.', 'recipe')


        return is_valid