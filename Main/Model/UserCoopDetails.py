from enum import unique
from  Main.DAC.config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class user_coop_details(db.DynamicDocument):
    User = db.ReferenceField('User', reverse_delete_rule=db.PULL)
    Coop = db.ReferenceField('Coop', reverse_delete_rule=db.PULL)
    meta = {'indexes':[
        {'fields' : ('User','Coop'), 'unique':True}
        ]} #enforces compund key ( the combination)
    Status = db.StringField(required=True)
    