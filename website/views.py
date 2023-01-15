# Here i will be storing the routes(location) of my website visible to the user

from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Diabetes, User, Heart
from . import db
import pickle
import pandas as pd
import numpy as np


views = Blueprint('views', __name__)

@views.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home2.html")


@views.route("/diabetes", methods=['GET', 'POST'])
@login_required
def diabetes():
    if request.method == 'GET':
        return render_template('diabetes_pred.html')
    else:
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])

        model1 = pickle.load(open('model/diabetes_final_model.pkl','rb'))
        input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        input_data_as_numpy_array= np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        print(input_data_reshaped)
        prediction = model1.predict(input_data_reshaped)
        senddata=""
        predi = ""
        if (prediction[0]== 0):
            senddata='According to the given details person does not have Diabetes'
            predi = "Not Diabetic"
        else:
            senddata='According to the given details chances of having Diabetes are High, So Please Consult a Doctor'
            predi = "Diabetic"
        new_data = Diabetes(pregnancies=Pregnancies, 
                            glucose=Glucose,
                            bloodpressure=BloodPressure,
                            skinthichness=SkinThickness,
                            insulin=Insulin,
                            bmi=BMI,
                            dpf=DiabetesPedigreeFunction,
                            age=Age,
                            outcome=predi,
                            user_id=current_user.id)
        db.session.add(new_data)
        db.session.commit()

        return render_template('diabetes_pred.html', prediction_text=senddata)

@views.route("/diabetes_history")
@login_required
def diabetes_history():
    return render_template('diabetes_history.html', user=current_user)


@views.route("/heart", methods=['GET', 'POST'])
@login_required
def heart():
    if request.method == 'GET':
        return render_template('heart_pred.html')
    else:
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'] )
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope']) 
        ca = int(request.form['ca'])
        thal= int(request.form['thal'])

        model_heart = pickle.load(open('model/heart_final_model.pkl', 'rb'))
        input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

        print(input_data)

        input_data_as_numpy_array= np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        print(input_data_reshaped)
        
        prediction = model_heart.predict(input_data_reshaped)
        senddata=""
        if (prediction[0]== 0):
            predi="No Heart Disease"
            senddata='According to the given details person does not have any Heart Diesease.'
        else:
            predi="Heart Disease"
            senddata='According to the given details chances of having Heart Diesease are High, So Please Consult a Doctor'

        new_data = Heart(age=age,
                        sex=sex,
                        cp=cp,
                        trestbps=trestbps,
                        chol=chol,
                        fbs=fbs,
                        restecg=restecg,
                        thalach=thalach,
                        exang=exang,
                        oldpeak=oldpeak,
                        slope=slope,
                        ca=ca,
                        thal=thal,
                        outcome=predi,
                        user_id=current_user.id)
        db.session.add(new_data)
        db.session.commit()
        return render_template('heart_pred.html', prediction_text=senddata)

@views.route("/heart_history")
@login_required
def heart_history():
    return render_template('heart_history.html', user=current_user)