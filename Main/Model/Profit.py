from Main.DAC.config import db

class Profit(db.DynamicDocument):
    Coopid = db.StringField(required=True)
    Month = db.StringField(required=True)
    Week = db.StringField(required=True)
    Year = db.StringField(required=True)
    Profit = db.StringField(required=True)
