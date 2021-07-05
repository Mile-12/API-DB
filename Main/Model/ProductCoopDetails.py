from enum import unique
from  Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class product_coop_details(db.DynamicDocument):
    Createdby = db.ReferenceField('User', reverse_delete_rule=db.PULL)
    Coop = db.ReferenceField('Coop', reverse_delete_rule=db.PULL)
    Product = db.ReferenceField('Product', reverse_delete_rule=db.PULL)
    