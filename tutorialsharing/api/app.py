from flask import Flask

from tutorialsharing.api.links import links_api
from tutorialsharing.api.users import users_api


app = Flask(__name__)
app.register_blueprint(links_api)
app.register_blueprint(users_api)

@app.route('/', methods=['GET'])
def get_home():
    return "WELCOME"
    # get links associated with a user
