from flask import Flask
from flask_cors import CORS, cross_origin
from tutorialsharing.secret import secret_key


from tutorialsharing.api.links import links_api
from tutorialsharing.api.users import users_api


app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(links_api)
app.register_blueprint(users_api)


CORS(app)


@app.route('/', methods=['GET'])
def get_home():
    return "WELCOME"
    # get links associated with a user

