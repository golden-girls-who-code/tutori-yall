from api import app


@app.route('/users', methods=['POST'])
def create_user():
    pass


@app.route('/users', methods=['PUT'])
def update_user():
    pass


@app.route('/users', methods=['GET'])
def get_user():
    pass
