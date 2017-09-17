import os


db_uri = os.environ.get('MONGODB_URI')
if not db_uri:
    db_uri = 'mongodb://localhost:27017'
