from api import app


@app.route('/links', methods=['POST'])
def create_link():
    #TODO: get requests object
    obj = {'username': username,
           'title': title,
           'url': url,
           'tags': tags.split(',')}

    if description:
        obj['description'] = description

    # TODO response
    connection.save(obj)

    return response


@app.route('/links', methods=['PUT'])
def update_link():
    pass


@app.route('/links', methods=['DELETE'])
def delete_link():
    pass


@app.route('/links', methods=['GET'])
def get_link():
    # get links associated with a user
    pass
