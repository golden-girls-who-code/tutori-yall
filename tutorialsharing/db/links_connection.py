from bson.objectid import ObjectId

from tutorialsharing.db.db_connection import DBConnection


class LinksConnection(DBConnection):

    def __init__(self, host, port):
        super(LinksConnection, self).__init__(host, port, 'users')
        # TODO: indexes

    def create_link(self, username, title, url, tags, description=None):
        """ Creates a link.

            Params:
                username (str): The username.
                title (str): Title of the tutorial url.
                url (str): The url of the tutorial.
                tags (list): A list of strings.
                description (str): Description of the tutorial (optional).
        """

        link = {'username': username,
                'title': title,
                'url': url,
                'tags': tags}

        if description:
            link['description']

        return self.connection.insert_one(link)

    def get_link(self, object_id):
        query = {'_id': ObjectId(object_id)}
        return self.connection.find_one(query)

    def get_links(self, username, tags=None):
        query = {}

        # TODO: have to get similar users first

        if tags:
            # this is an AND operation
            # all tags must be contained in the tags field
            query = {'tags': {'$all': tags}}

        links = self.connection.find(query)
        return links

    def update_link(self, object_id):
        pass

    def delete_link(self, object_id):
        query = {'_id': ObjectId(object_id)}
        return self.connection.remove_one(query)
