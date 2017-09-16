from api import app


@app.route('/users', methods=['POST'])
def create_user():

    if request.method == 'POST':
        user = request.form['username']
        years_of_dev = request.form['years_of_development']


@app.route('/users', methods=['PUT'])
def update_user():

    if request.method == 'PUT':
        user = request.form['username']
        years_of_dev = request.form['years_of_development']


@app.route('/users', methods=['GET'])
def get_user():
    if request.method == 'GET':
        user = request.form['username']
    
