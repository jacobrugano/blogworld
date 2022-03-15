from . import db 
from sql_alchemy_sql import func
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Interger, primary_key = True)
    email = db.Column(db.String(200), unique = True)
    username = db.Column(db.String(200), unique = True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.Date(timezone=True), default = func.now)


