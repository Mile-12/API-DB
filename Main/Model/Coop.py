from  Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Coop(db.Document):
    
    Coopid = db.StringField(primary_key=True,required=True, unique=True)
    image = db.ImageFeild()
    Name = db.StringField(required=True, unique=True)
    Leader = db.ReferenceField('User')
    Members = db.ListField(db.ReferenceField('User', reverse_delete_rule=db.PULL))
    Products = db.ListField(db.ReferenceField('Products', reverse_delete_rule=db.PULL))