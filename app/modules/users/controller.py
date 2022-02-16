# Import flask core dependencies
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, request, jsonify
from app import db

# Import Model and Schema
from app.modules.users.model import Users
from app.modules.users.schema import UserSchema

# Import necessary helpers
from app.helpers.main_helper import send_response

# Define the blueprint: 'auth', set its url prefix: app.url/auth
users = Blueprint('users', __name__, url_prefix='/users')

# Init Schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users.route('/', methods=['GET'])
def get_all_users():
    users = Users.query.all()

    datas = users_schema.dump(users)

    return send_response('Retrieve Success', datas, 200)

@users.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.get(user_id)

    data = user_schema.dump(user)

    return send_response('Retrieve Success', data, 200)

@users.route('/create_user', methods=['POST'])
def create_user():
    name        = request.json['name']
    email       = request.json['email']
    password    = generate_password_hash(request.json['password'], 'sha256')

    new_user = Users(name, email, password)

    db.session.add(new_user)
    db.session.commit()

    data = user_schema.dump(new_user)

    return send_response('Insert Success', data, 200)

@users.route('/update_user/<user_id>', methods=['POST'])
def update_user(user_id):
    user = Users.query.get(user_id)

    user.name     = request.json['name'] if 'name' in request.json else user.name
    user.email    = request.json['email'] if 'email' in request.json is not None else user.email
    user.password = generate_password_hash(request.json['password'], 'sha256') if 'password' in request.json is not None else user.password

    db.session.commit()

    data = user_schema.dump(user)

    return send_response('Update Success', data, 200)

@users.route('/delete_user/<user_id>', methods=['POST'])
def delete_user(user_id):
    user = Users.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return send_response('Delete Success', '', 200)