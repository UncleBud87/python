
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninja = []
        for u in results:
            ninja.append( cls(u) )
        return ninja

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def dojos_ninjas(cls,data):
        query = "select * From ninjas WHERE dojos_id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results