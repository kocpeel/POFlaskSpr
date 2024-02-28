from flask import jsonify, request, abort
from models import User

class Controllers:
    def __init__(self):
        self.users = {
            1: User('John', 'Doe', 1990, 'user'),
            2: User('Jane', 'Doe', 1995, 'premium'),
            3: User('Admin', 'User', 1985, 'admin')
        }

    def validate_user(self, user):
        valid_groups = ['user', 'premium', 'admin']
        if 'firstName' not in user or 'lastName' not in user or 'birthYear' not in user or 'group' not in user:
            return False
        if user['group'] not in valid_groups:
            return False
        return True

    def get_all_users(self):
        return jsonify({'users': [user.to_dict() for user in self.users.values()]})

    def get_user(self, user_id):
        if user_id not in self.users:
            abort(404)
        return jsonify(self.users[user_id].to_dict())

    def create_user(self):
        if not request.json or not self.validate_user(request.json):
            abort(400)
        user_id = len(self.users) + 1
        self.users[user_id] = User(**request.json)
        return jsonify({'id': user_id}), 201

    def update_user(self, user_id):
        if user_id not in self.users:
            abort(404)
        if not request.json or not self.validate_user(request.json):
            abort(400)
        self.users[user_id].__dict__.update(request.json)
        return '', 204

    def delete_user(self, user_id):
        if user_id not in self.users:
            abort(404)
        del self.users[user_id]
        return '', 204
