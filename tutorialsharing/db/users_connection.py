from pymongo import ASCENDING

from tutorialsharing.db.db_connection import DBConnection


class UsersConnection(DBConnection):

    def __init__(self, uri):
        super(UsersConnection, self).__init__(uri, 'users')
        self._init_indexes()

    def _init_indexes(self):
        self.connection.create_index([('userid', ASCENDING)], unique=True)
        self.connection.create_index([('years_of_development', ASCENDING)])

    def save_user(self,
                  userid,
                  username=None,
                  name=None,
                  avatar_url=None,
                  years_of_development=None):

        query = {'userid': userid}
        update_vals = {'userid': userid}

        if username:
            update_vals['username'] = username

        if name:
            update_vals['name'] = name

        if avatar_url:
            update_vals['avatar_url'] = avatar_url

        if years_of_development:
            update_vals['years_of_development'] = int(years_of_development)

        results = self.connection.update(query, {'$set': update_vals}, upsert=True)
        return results

    def get_user(self, userid):
        user = self.connection.find_one({"userid": userid})
        return user

    def get_users(self):
        users = self.connection.find()
        return users

    def get_similar_users(self, userid):
        user = self.get_user(userid)

        # create years range
        yod = user['years_of_development']
        ll = int(yod) - 1 # lower limit
        ul = int(yod) + 1 # upper limit

        # query for similar users in years range
        query = {"years_of_development": {"$gte": ll, "$lte": ul}}
        similar_users = self.connection.find(query)

        # TODO: don't want to return the original user info
        return similar_users
