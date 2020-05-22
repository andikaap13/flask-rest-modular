# Import flask core dependencies
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, request, jsonify
from app import db

# Import Model and Schema
from app.modules.users.schema import UserSchema
from app.modules.users.model import Users

# Import necessary helpers
from app.helpers.main_helper import *


# Define the blueprint: 'auth', set its url prefix: app.url/auth
users = Blueprint('users', __name__, url_prefix='/users')

# Init Schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users.route('/', methods=['GET'])
def get_all_users():
    users = Users.query.all()

    datas = users_schema.dump(users)

    return send_response(message='Retrieve Success', data=datas, code=200)