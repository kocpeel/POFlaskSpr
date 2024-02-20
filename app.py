from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)



#     Model użytkownika dodawany w aplikacji powinien być zgodny z następującym JSON:
# {
#     "firstName": str,
#     "lastName": str,
#     "birthYear": int,
#     "group": str, // jedynymi poprawnymi wartościami są napisy: "user", "premium", "admin"
   
# }

# Model użytkownika zwracany z aplikacji powinien być zgodny z następującym JSON:
# {
#     "id": int,
#     "firstName": str,
#     "lastName": str,
#     "age": int,
#     "group": str, // jedynymi poprawnymi wartościami są napisy: "user", "premium", "admin"
   
# }


users = {
    1: {
        'firstName': 'John',
        'lastName': 'Doe',
        'birthYear':  1990,
        'group': 'user'
    },
    2: {
        'firstName': 'Jane',
        'lastName': 'Doe',
        'birthYear':  1995,
        'group': 'premium'
    },
    3: {
        'firstName': 'Admin',
        'lastName': 'User',
        'birthYear':  1985,
        'group': 'admin'
    }
}


def validate_user(user):
    valid_groups = ['user', 'premium', 'admin']
    if 'firstName' not in user or 'lastName' not in user or 'birthYear' not in user or 'group' not in user:
        return False
    if user['group'] not in valid_groups:
        return False
    return True

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify({'users': users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        abort(404)
    user = users[user_id]
    age = datetime.now().year - user['birthYear']
    return jsonify({
        'id': user_id,
        'firstName': user['firstName'],
        'lastName': user['lastName'],
        'age': age,
        'group': user['group']
    })


@app.route('/users', methods=['POST']) 
def create_user(): # half was commited
    if not request.json or not validate_user(request.json):
        abort(400)
    user_id = len(users) +  1
    users[user_id] = {
        'firstName': request.json['firstName'],
        'lastName': request.json['lastName'],
        'birthYear': request.json['birthYear'],
        'group': request.json['group']
    }
    return jsonify({'id': user_id}),  201


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    if user_id not in users:
        abort(404)
    if not request.json or not validate_user(request.json):
        abort(400)
    users[user_id].update(request.json)
    return '',  204
