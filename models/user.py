from config.mysqlconnection import connectToMySQL


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
    def add_user(csl, data):
        query = """
        INSERT INTO users(  first_name, last_name, email  )
        VALUES(  %(first_name)s , %(last_name)s, %(email)s  );
        """

        return connectToMySQL('users_schema').query_db(query, data)
    
