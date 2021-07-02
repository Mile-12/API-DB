from  Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.DynamicDocument):
    UID = db.StringField(required=True, unique=True)
    #image = db.ImageFeild()
    mobile = db.StringField(required=True, unique=True)
    username = db.StringField(required=True, unique=True)
    _password = db.StringField(required=True)

    def hash_password(self):
        self._password = generate_password_hash(self._password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self._password, password)