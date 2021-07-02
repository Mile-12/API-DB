from  Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Coop(db.Document):
    
    Coopid = db.StringField(required=True, unique=True)
    Name = db.StringField(required=True, unique=True)
    #Products = db.ListField(db.ReferenceField('Products', reverse_delete_rule=db.PULL))