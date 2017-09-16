from pymongo import MongoClient


class DBConnection(object):

    def __init__(self, host, port, collection_name):
        # TODO: username and password?
        client = MongoClient(host, port)
        db = client['app']
        self.connection = db[collection_name]
