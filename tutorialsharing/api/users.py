from flask import Blueprint, request

from tutorialsharing.db.users_connection import UsersConnection


users_api = Blueprint('users_api', __name__)


db_host = 'localhost'
db_port = 27017
links_connection = UsersConnection(db_host, db_port)


@users_api.route('/users', methods=['POST'])
def create_user():

    if request.method == 'POST':
        user = request.form['username']
        years_of_dev = request.form['years_of_development']


@users_api.route('/users', methods=['PUT'])
def update_user():

    if request.method == 'PUT':
        user = request.form['username']
        years_of_dev = request.form['years_of_development']


@users_api.route('/users', methods=['GET'])
def get_user():
    if request.method == 'GET':
        user = request.form['username']
