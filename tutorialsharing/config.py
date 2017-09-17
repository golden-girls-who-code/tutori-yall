import os


db_uri = os.environ.get('MONGODB_URI')
if not db_uri:
    db_uri = 'mongodb://localhost:27017'

db_name = os.environ.get('DBNAME', None)
if not db_name:
    db_name = 'app'

db_username = os.environ.get('DBUN', None)
db_password = os.environ.get('DBPW', None)
