from flask import Flask
from controllers import Controllers

app = Flask(__name__)
controllers = Controllers()

@app.route('/users', methods=['GET'])
def users_get():
    return controllers.get_all_users()

@app.route('/users/<int:user_id>', methods=['GET'])
def user_get(user_id):
    return controllers.get_user(user_id)

@app.route('/users', methods=['POST'])
def user_post():
    return controllers.create_user()

@app.route('/users/<int:user_id>', methods=['PATCH'])
def user_patch(user_id):
    return controllers.update_user(user_id)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    return controllers.delete_user(user_id)

if __name__ == '__main__':
    app.run(debug=True)
    
# dla plików models i controllers nie ma historii commitów by nie zepsuć kodu,
# którego logika była przepisywana na warstwy
