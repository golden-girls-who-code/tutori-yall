from bson.objectid import ObjectId
from pymongo import ASCENDING

from tutorialsharing.db.db_connection import DBConnection
from tutorialsharing.db.users_connection import UsersConnection


class LinksConnection(DBConnection):

    def __init__(self, uri, db_name, username=None, password=None):
        super(LinksConnection, self).__init__(uri,
                                              db_name,
                                              'links',
                                              username=username,
                                              password=password)

        self._users_connection = UsersConnection(uri, db_name)
        self._init_indexes()

    def _init_indexes(self):
        self.connection.create_index([('userid', ASCENDING)])
        self.connection.create_index([('tags', ASCENDING)])

    def save_link(self, userid, title, url, tags, description=None):
        """ Creates or updates a link.

            Params:
                userid (str): The userid.
                title (str): Title of the tutorial url.
                url (str): The url of the tutorial.
                tags (list): A list of strings.
                description (str): Description of the tutorial (optional).
        """
        query = {'userid': userid, 'url': url}

        update_vals = {'userid': userid,
                       'title': title,
                       'url': url,
                       'tags': tags}

        if description:
            update_vals['description'] = description

        results = self.connection.update(query, {'$set': update_vals}, upsert=True)
        return results

    def get_link(self, object_id):
        query = {'_id': ObjectId(object_id)}
        return self.connection.find_one(query)

    def get_links(self, userid, tags=None, limit=100):
        query = {'userid': userid}

        if tags:
            # this is an AND operation meaning
            # all tags must be contained in the tags field
            query = {'tags': {'$all': tags}}

        cursor = self.connection.find(query).limit(limit)
        return cursor

    def get_all_links(self, tags=None, limit=100):
        query = {}

        if tags:
            # this is an AND operation meaning
            # all tags must be contained in the tags field
            query = {'tags': {'$all': tags}}

        cursor = self.connection.find(query).limit(limit)
        return cursor

    def get_links_of_similar_users(self, userid, tags=None, limit=100):
        query = {'userid': userid}

        if tags:
            # this is an AND operation meaning
            # all tags must be contained in the tags field
            query = {'tags': {'$all': tags}}

        # TODO: revisit this, this is really bad code
        links = []
        user_cursor = self._users_connection.get_similar_users(userid)

        for user in user_cursor:
            other_userid = user['userid']
            if other_userid == userid:
                continue

            query['userid'] = other_userid
            cursor = self.connection.find(query).limit(limit)

            for link in cursor:
                links.append(link)

        return links

    def delete_link(self, object_id):
        query = {'_id': ObjectId(object_id)}
        return self.connection.remove_one(query)
