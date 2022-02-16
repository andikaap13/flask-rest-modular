# Import the database object (db) from the main application module
from app import db

# Import base model
from app.modules.base.model import Base

import uuid

# Define a User model
class Users(Base):
    public_id   = db.Column(db.String(64), nullable=False, unique=True)
    name        = db.Column(db.String(64), nullable=False)
    email       = db.Column(db.String(64), nullable=False, unique=True)
    password    = db.Column(db.String(128), nullable=False)
    admin       = db.Column(db.Boolean, nullable=False, default=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):
        self.public_id  = uuid.uuid4().hex
        self.name       = name
        self.email      = email
        self.password   = password

    def __repr__(self):
        return '<User %r>' % (self.name)