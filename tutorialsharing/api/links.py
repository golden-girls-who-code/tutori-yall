from flask import Blueprint

from tutorialsharing.db.links_connection import LinksConnection


links_api = Blueprint('links_api', __name__)


db_host = 'localhost'
db_port = 27017
links_connection = LinksConnection(db_host, db_port)


@links_api.route('/links', methods=['POST'])
def create_link():

    # required args
    username = requests.args['username']
    title = requests.args['title']
    url = requests.args['url']
    tags = requests.args['tags'].split(',')

    # optional args
    description = requests.args['description']

    if description:
        description = str(description)

    links_connection.create_link(username, title, url, tags, description=description)

    # TODO response
    return response


@links_api.route('/links', methods=['GET'])
def get_link():
    return "LINKS"
    # get links associated with a user


@links_api.route('/links', methods=['PUT'])
def update_link():
    pass


@links_api.route('/links', methods=['DELETE'])
def delete_link():
    pass