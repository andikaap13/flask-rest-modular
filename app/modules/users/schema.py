# Import ORM used by the app
from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('public_id', 'name', 'email', 'admin')