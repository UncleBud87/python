from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re

class Recipe():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_recipe(cls,data):
        query = 'INSERT INTO recipes (name, description, instructions, under_30_min, created_at) VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30_min)s,%(created_at)s);'

        result = connectToMySQL('recipes_schema')