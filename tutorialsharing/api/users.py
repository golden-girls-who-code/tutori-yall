import requests
import os

from bson import json_util
from flask import Blueprint, request, jsonify

try:
    from tutorialsharing.secret import client_secret, client_id
except:
    client_secret = os.environ['AUTHCLIENT']
    client_id = os.environ['AUTHCLIENTID']

from tutorialsharing.config import db_uri, db_username, db_password
from tutorialsharing.db.users_connection import UsersConnection


users_api = Blueprint('users_api', __name__)
users_connection = UsersConnection(db_uri,
                                   username=db_username,
                                   password=db_password)


@users_api.route('/users', methods=['POST'])
def create_user():
    json_request_object = request.get_json()

    # required
    userid = json_request_object['userid']

    # optional
    username = json_request_object.get('username')
    name = json_request_object.get('name')
    avatar_url = json_request_object.get('avatar_url')
    years_of_development = json_request_object.get('years_of_development')

    if years_of_development:
        years_of_development = int(years_of_development)

    results = users_connection.save_user(userid,
                                         username=username,
                                         name=name,
                                         avatar_url=avatar_url,
                                         years_of_development=years_of_development)
    return json_util.dumps(results)


@users_api.route('/users/<userid>', methods=['GET'])
def get_user(userid):
    return json_util.dumps({'user': users_connection.get_user(userid)})


@users_api.route('/users', methods=['GET'])
def get_users():
    return json_util.dumps({'users': users_connection.get_users()})


@users_api.route('/users', methods=['PUT'])
def update_user():
    pass


@users_api.route('/login', methods=['POST'])
def login():
    code = request.get_json()['code']
    post_data = {'client_id': client_id,
                 'client_secret':  client_secret,
                 'code': code}
    response = requests.post('https://github.com/login/oauth/access_token', data=post_data)
    print response.text
    # access_token = dict(parse_qs(response.text))['access_token'][0]
    access_token = response.text.split('&')[0].split('=')[1]
    user_info = requests.get('https://api.github.com/user?access_token={}'.format(access_token)).json()
    resp = jsonify(username= user_info['login'],
                   user_id=str(user_info['id']),
                   avatar_url=user_info['avatar_url'])
    return resp
