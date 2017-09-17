from bson import json_util
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


@links_api.route('/links/<userid>', methods=['GET'])
def get_links(userid):

    tags = request.args.get('tags')
    if tags:
        tags = tags.split(',')

    limit = int(request.args.get('limit', 100))

    cursor = links_connection.get_links(userid, tags=tags, limit=limit)
    return json_util.dumps(list(cursor))


@links_api.route('/links', methods=['PUT'])
def update_link():
    pass


@links_api.route('/links', methods=['DELETE'])
def delete_link():
    pass
