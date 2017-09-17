from bson import json_util
from flask import Blueprint, request

try:
    from tutorialsharing.override_config import db_uri
except:
    from tutorialsharing.config import db_uri
from tutorialsharing.db.links_connection import LinksConnection


links_api = Blueprint('links_api', __name__)
links_connection = LinksConnection(db_uri)


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

    results = links_connection.save_link(userid,
                                         title,
                                         url,
                                         tags,
                                         description=description)

    return json_util.dumps(results)


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
