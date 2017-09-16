from flask import Blueprint

from tutorialsharing.db.links_connection import LinksConnection


users_api = Blueprint('users_api', __name__)


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