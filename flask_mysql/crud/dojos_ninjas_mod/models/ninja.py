
from dojos_ninjas_mod.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninja = []
        for u in results:
            ninja.append( cls(u) )
        return ninja

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)