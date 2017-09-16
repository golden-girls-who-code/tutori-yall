from flask import requests

from api import app
from tutorialsharing.db.links_connection import LinksConnection


host = 'localhost'
port = 27017
links_connection = LinksConnection(host, port)


@app.route('/links', methods=['POST'])
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


@app.route('/links', methods=['GET'])
def get_link():
    # get links associated with a user
    pass


@app.route('/links', methods=['PUT'])
def update_link():
    pass


@app.route('/links', methods=['DELETE'])
def delete_link():
    pass
