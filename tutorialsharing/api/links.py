from flask import Blueprint, request

from tutorialsharing.db.links_connection import LinksConnection


links_api = Blueprint('links_api', __name__)


db_host = 'localhost'
db_port = 27017
links_connection = LinksConnection(db_host, db_port)


@links_api.route('/links/<userid>', methods=['POST'])
def create_link(userid):
    # TODO: if err, send response msg
    json_request_object = request.get_json()

    # required args
    title = json_request_object['title']
    url = json_request_object['url']
    tags = json_request_object['tags']

    # optional args
    description = json_request_object.get('description')

    if description:
        description = str(description)

    link_id = links_connection.create_link(userid,
                                           title,
                                           url,
                                           tags,
                                           description=description)

    return link_id


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
