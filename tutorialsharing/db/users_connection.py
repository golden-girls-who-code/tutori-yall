from tutorialsharing.db.db_connection import DBConnection


class UsersConnection(DBConnection):

    def __init__(self, host, port):
        super(UsersConnection, self).__init__(host, port, 'users')

    def create_user(self, userid, username, years_of_development):
        user = {'userid': userid,
                'username': username,
                'years_of_development': int(years_of_development)}

        _id = self.connection.insert_one(user)
        return str(_id)

    def get_user(self, userid):
        user = self.connection.find_one({"userid": userid})
        return user

    def get_users(self):
        users = self.connection.find()
        return users

    def get_similar_users(self, username):
        user = self.get_user(username)

        # create years range
        yod = user['years_of_development']
        ll = int(yod) - 1 # lower limit
        ul = int(yod) + 1 # upper limit

        # query for similar users in years range
        query = {"years_of_development": {"$gte": ll, "$lte": ul}}
        similar_users = self.connection.find(query)
        return users

    def update_user(self, username, years_of_development):
        query = {'username': username}
        update_vals = {'years_of_development': years_of_development}
        return self.connection.upsert(query, update_vals)
