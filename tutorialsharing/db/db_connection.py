from pymongo import MongoClient


class DBConnection(object):

    def __init__(self,
                 uri,
                 db_name,
                 collection_name,
                 username=None,
                 password=None):
        # TODO: username and password?
        client = MongoClient(uri)
        db = client[db_name]
        if username and password:
            db.authenticate(username, password)
        self.connection = db[collection_name]
