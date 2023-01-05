# Here i will be storing the routes(location) of my website visible to the user

from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Diabetes
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
        Pregnancies = request.form['Pregnancies']
        Glucose = request.form['Glucose']
        BloodPressure = request.form['BloodPressure']
        SkinThickness = request.form['SkinThickness']
        Insulin = request.form['Insulin']
        BMI = request.form['BMI']
        DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction']
        Age = request.form['Age']

        model1 = pickle.load(open('model/diabetes_final_model.pkl','rb'))
        input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        print(input_data)
        input_data_as_numpy_array= np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        prediction = model1.predict(input_data_reshaped)
        senddata=""
        if (prediction[0]== 0):
            senddata='According to the given details person does not have Diabetes'
        else:
            senddata='According to the given details chances of having Diabetes are High, So Please Consult a Doctor'
        return render_template('diabetes_pred.html', prediction_text=senddata)

