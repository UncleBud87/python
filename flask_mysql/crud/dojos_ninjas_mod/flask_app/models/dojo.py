
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_dojos_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('ninjas').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["ninjas.first_name"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojo = []
        for u in results:
            dojo.append( cls(u) )
        return dojo

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
