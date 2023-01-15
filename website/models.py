from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Diabetes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # To auto set date
    pregnancies = db.Column(db.Integer)
    glucose = db.Column(db.Integer)
    bloodpressure = db.Column(db.Integer)
    skinthichness = db.Column(db.Integer)
    insulin = db.Column(db.Integer)
    bmi = db.Column(db.Integer)
    dpf = db.Column(db.Integer)
    age = db.Column(db.Integer)
    outcome = db.Column(db.String(10000))
    # Getting user(Foreign Key), Here we get the user by it's ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # not here

class Heart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    age = db.Column(db.Integer)
    sex = db.Column(db.String(8))
    cp = db.Column(db.String(4))
    tresbps = db.Column(db.Integer)
    chol = db.Column(db.Integer)
    fbs = db.Column(db.String(2))
    restecg = db.Column(db.String(3))
    thalach = db.Column(db.Integer)
    exang = db.Column(db.String(2))
    oldpeak = db.Column(db.Float(3))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    diabetes = db.relationship('Diabetes') # Add the id of different Notes (capatilize table letter required)