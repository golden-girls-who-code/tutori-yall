from bson import json_util
from flask import Blueprint, request

from tutorialsharing.db.users_connection import UsersConnection


users_api = Blueprint('users_api', __name__)


db_host = 'localhost'
db_port = 27017
users_connection = UsersConnection(db_host, db_port)


@users_api.route('/users', methods=['POST'])
def create_user():
    json_request_object = request.get_json()

    userid = json_request_object['userid']
    username = json_request_object['username']
    years_of_development = int(json_request_object['years_of_development'])

    # need to check if that user exists first
    if users_connection.get_user(userid):
        # TODO: return status code, msg
        return "User already exists"

    return users_connection.create_user(userid, username, years_of_development)


@users_api.route('/users/<userid>', methods=['GET'])
def get_user(userid):
    return json_util.dumps({'user': users_connection.get_user(userid)})


@users_api.route('/users', methods=['GET'])
def get_users():
    return json_util.dumps({'users': users_connection.get_users()})


@users_api.route('/users', methods=['PUT'])
def update_user():
    pass
