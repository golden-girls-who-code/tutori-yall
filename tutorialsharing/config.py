import os


db_uri = os.environ.get('MONGODB_URI')
if not db_uri:
    db_uri = 'mongodb://localhost:27017'

db_username = os.environ.get('DBUN', None)
db_password = os.environ.get('DBPW', None)
