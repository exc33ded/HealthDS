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
    trestbps = db.Column(db.Integer)
    chol = db.Column(db.Integer)
    fbs = db.Column(db.String(2))
    restecg = db.Column(db.String(3))
    thalach = db.Column(db.Integer)
    exang = db.Column(db.String(2))
    oldpeak = db.Column(db.Float(3))
    slope = db.Column(db.String(3))
    ca = db.Column(db.String(5))
    thal = db.Column(db.String(4))
    outcome = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class BCancer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    radius_mean = db.Column(db.Float(100))
    texture_mean = db.Column(db.Float(100))
    perimeter_mean = db.Column(db.Float(100))
    area_mean = db.Column(db.Float(100))
    smoothness_mean = db.Column(db.Float(100))
    compactness_mean = db.Column(db.Float(100))
    concavity_mean = db.Column(db.Float(100))
    concave_points_mean = db.Column(db.Float(100))
    symmetry_mean = db.Column(db.Float(100))
    fractal_dimension_mean = db.Column(db.Float(100))
    outcome = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Liver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    Age = db.Column(db.Integer)
    sex = db.Column(db.String(8))
    Total_Bilirubin = db.Column(db.Float(100))
    Direct_Bilirubin = db.Column(db.Float(100))
    Alkaline_Phosphotase = db.Column(db.Integer)
    Alamine_Aminotransferase = db.Column(db.Integer)
    Aspartate_Aminotransferase = db.Column(db.Integer)
    Total_Protiens = db.Column(db.Float(100))
    Albumin = db.Column(db.Float(100))
    Albumin_and_Globulin_Ratio = db.Column(db.Float(100))
    outcome = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    diabetes = db.relationship('Diabetes') # Add the id of different Notes (capatilize table letter required)
    heart = db.relationship('Heart')
    bcancer = db.relationship('BCancer')
    liver = db.relationship('Liver')

    def __repr__(self):
        return '<Name %r>' % self.name