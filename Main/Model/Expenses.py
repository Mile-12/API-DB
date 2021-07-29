from Main.DAC.config import db

class Expenses(db.DynamicDocument):
    Coopid = db.StringField(required=True)
    Location = db.StringField(required=True)
    ProductName = db.StringField(required=True)
    Amount = db.StringField(required=True)
    Date = db.StringField(required=True)

    


