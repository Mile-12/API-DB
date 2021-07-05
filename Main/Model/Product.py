from  Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Product(db.Document):
    Name = db.StringField(required=True)
    Description = db.StringField()
    Price = db.StringField(required=True)
    Quantity = db.StringField(required=True, unique=True)