from pymongo import MongoClient


class DBConnection(object):

    def __init__(self, uri, collection_name, username=None, password=None):
        # TODO: username and password?
        client = MongoClient(uri)
        db = client['app']
        if username and password:
            db.authenticate(username, password)
        self.connection = db[collection_name]
