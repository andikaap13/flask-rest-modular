# Import the database object (db) from the main application module
from app import db

# Import base models
from app.modules.base.models import Base

# Define a User model
class Users(Base):
    public_id   = db.Column(db.String(64), nullable=False, unique=True)
    email       = db.Column(db.String(128), nullable=False, unique=True)
    name        = db.Column(db.String(128), nullable=False)
    password    = db.Column(db.String(128), nullable=False)
    admin       = db.Column(db.Boolean)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)               