from flask_app.config.mysqlconnection import connectToMySQL


class Password:
    def __init__(self, data):
        self.id = data['id']
        self.password = data['password']
        self.user_id = data['user_id']