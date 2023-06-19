from flask_app.config.mysqlconnection import connectToMySQL


class User:
    DB = "users_schema"

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_users(cls):
        query = """
        SELECT *
        FROM Users;
        """

        results = connectToMySQL("users_schema").query_db(query)

        all_users = []

        for user in results:

            all_users.append(cls(user))

        return all_users
    
    @classmethod
    def get_user(cls, data):
        query = """
        SELECT *
        FROM users
        WHERE id = %(user_id)s ;
        """

        results = connectToMySQL('users_schema').query_db(query, data)

        return cls(results[0])

    @classmethod
    def add_user(data):
        query = """
        INSERT INTO users(  first_name, last_name, email  )
        VALUES(  %(first_name)s , %(last_name)s, %(email)s  );
        """

        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def edit_user(data):
        query = """
        UPDATE users
        SET first_name= %(first_name)s , last_name= %(last_name)s, email= %(email)s;
        WHERE id = %(user_id)s;
        """

        results = connectToMySQL('users_schema').query_db(query, data)
        return results
    
    @classmethod
    def delete_user(user_id):
        query = """"
        DELETE FROM users
        WHERE id = %(id)s;
        """
        data = {'id': user_id}

        results = connectToMySQL('users_schema').query_db(query, data)

        return results
