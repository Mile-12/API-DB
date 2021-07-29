from Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash


class purchase_History(db.DynamicDocument):
    coopid = db.StringField(required=True)
    ProductName = db.StringField(required=True)
    Price = db.StringField(required=True)
    Quantity = db.StringField(required=True)
    CustomerName = db.StringField(required=True)
    CustomerContact = db.StringField(required=True)
