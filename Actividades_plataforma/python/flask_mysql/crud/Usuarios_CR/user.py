from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('esquema_usuarios').execute_query(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create(cls, first_name, last_name, email):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s);"
        data = (first_name, last_name, email)
        result = connectToMySQL('esquema_usuarios').execute_query(query, data)
        if result:
            new_user_id = result
            query = "SELECT * FROM users WHERE id = %s;"
            data = (new_user_id,)
            result = connectToMySQL('esquema_usuarios').execute_query(query, data)
            if result:
                return cls(result[0])
        return None