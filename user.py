from sqlalchemy import Column, Integer, String

from .u



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unik=True)
    password = db.Column(db.String(100), unik=True)
