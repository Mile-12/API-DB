from  Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    UID = db.StringField(required=True, unique=True)
    #image = db.ImageFeild()
    mobile = db.StringField(required=True, unique=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)