# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Marshmallow ORM
from flask_marshmallow import Marshmallow

# Import necessary helpers
from app.helpers.main_helper import send_response

# Import middlewares
from app.middlewares.auth import Auth

# Define the WSGI application object
app = Flask(__name__)

# Calling middlewares
app.wsgi_app = Auth(app.wsgi_app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Define Marshmallow ORM
ma = Marshmallow(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Hello World
@app.route('/')
def hello_world():
    return send_response('Hello World!', '', 200)

# Import a module / component using its blueprint handler variable (users)
from app.modules.users.controller import users

# Register blueprint(s)
app.register_blueprint(users)

# Build the database
db.create_all()