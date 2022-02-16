from flask import Blueprint, request, jsonify
from app import db

# Import Model and Schema
from app.modules.users.model import Users

# Import necessary helpers
from app.helpers.main_helper import send_response

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = Users.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return send_response('Login Success!', {'token' : token.decode('UTF-8')}, 200)
        
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})