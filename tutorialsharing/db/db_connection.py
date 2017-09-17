from pymongo import MongoClient


class DBConnection(object):

    def __init__(self, uri, collection_name):
        # TODO: username and password?
        client = MongoClient(uri)
        db = client['app']
        self.connection = db[collection_name]
