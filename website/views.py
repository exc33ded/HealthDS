# Here i will be storing the routes(location) of my website visible to the user

from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Diabetes, User, Heart, BCancer, Liver, User
from . import db
import pickle
import pandas as pd
import numpy as np

import sys
import os
import glob
import re
from werkzeug.utils import secure_filename

# Keras
from PIL import Image
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

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
        print(prediction[0])
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

        if sex == 1:
            gender="Male"
        else:
            gender="Female"

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
                        sex=gender,
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

@views.route("/bcancer", methods=['GET', 'POST'])
@login_required
def bcancer():
    if request.method == 'GET':
        return render_template('cancer_pred.html')
    else: 
        radius_mean = float(request.form['radius_mean'])
        texture_mean = float(request.form['texture_mean']) 
        perimeter_mean = float(request.form['perimeter_mean'])
        area_mean = float(request.form['area_mean']) 
        smoothness_mean = float(request.form['smoothness_mean']) 
        compactness_mean = float(request.form['compactness_mean']) 
        concavity_mean = float(request.form['concavity_mean'])
        concave_points_mean = float(request.form['concave_points_mean']) 
        symmetry_mean = float(request.form['symmetry_mean']) 
        fractal_dimension_mean = float(request.form['fractal_dimension_mean'])
        radius_se = float(request.form['radius_se']) 
        texture_se = float(request.form['texture_se']) 
        perimeter_se = float(request.form['perimeter_se']) 
        area_se = float(request.form['area_se']) 
        smoothness_se = float(request.form['smoothness_se'])
        compactness_se = float(request.form['compactness_se']) 
        concavity_se = float(request.form['concavity_se']) 
        concave_points_se = float(request.form['concave_points_se']) 
        symmetry_se = float(request.form['symmetry_se'])
        fractal_dimension_se = float(request.form['fractal_dimension_se']) 
        radius_worst = float(request.form['radius_worst']) 
        texture_worst = float(request.form['texture_worst'])
        perimeter_worst = float(request.form['perimeter_worst']) 
        area_worst = float(request.form['area_worst']) 
        smoothness_worst = float(request.form['smoothness_worst'])
        compactness_worst = float(request.form['compactness_worst']) 
        concavity_worst = float(request.form['concavity_worst']) 
        concave_points_worst = float(request.form['concave_points_worst'])
        symmetry_worst = float(request.form['symmetry_worst']) 
        fractal_dimension_worst = float(request.form['fractal_dimension_worst'])

        model_bcancer = pickle.load(open('model/cancer_final_model.pkl', 'rb'))
        input_data = (radius_mean, texture_mean, perimeter_mean,
                    area_mean, smoothness_mean, compactness_mean, concavity_mean,
                    concave_points_mean, symmetry_mean, fractal_dimension_mean,
                    radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                    compactness_se, concavity_se, concave_points_se, symmetry_se,
                    fractal_dimension_se, radius_worst, texture_worst,
                    perimeter_worst, area_worst, smoothness_worst,
                    compactness_worst, concavity_worst, concave_points_worst,
                    symmetry_worst, fractal_dimension_worst)

        print(input_data)

        input_data_as_numpy_array= np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        print(input_data_reshaped)

        prediction = model_bcancer.predict(input_data_reshaped)
        senddata=""
        if (prediction[0] == 0):
            predi = "Benign"
            senddata='According to the given details the patient have a chance of Benign Type Cancer.'
        else:
            predi = "Malignant"
            senddata='According to the given details the patient have a chance of Malignant Type Cancer.'

        new_data = BCancer(radius_mean=radius_mean,
                        texture_mean=texture_mean, 
                        perimeter_mean=perimeter_mean,
                        area_mean=area_mean,
                        smoothness_mean=smoothness_mean,
                        compactness_mean=compactness_mean, 
                        concavity_mean=concavity_mean,
                        concave_points_mean=concave_points_mean, 
                        symmetry_mean=symmetry_mean, 
                        fractal_dimension_mean=fractal_dimension_mean,
                        outcome=predi,
                        user_id=current_user.id)
        db.session.add(new_data)
        db.session.commit()

        return render_template('cancer_pred.html', prediction_text=senddata)

@views.route('/bcancer_history')
@login_required
def bcancer_history():
    return render_template('cancer_history.html', user=current_user)

@views.route('/liver', methods=['GET', 'POST'])
@login_required
def liver():
    if request.method == "GET":
        return render_template('liver_pred.html')
    else:
        Age = int(request.form['Age'])
        sex = int(request.form['sex'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])
        Direct_Bilirubin = float(request.form['Direct_Bilirubin'])
        Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])

        if sex == 1:
            gender="Male"
        else:
            gender="Female"

        model_liver = pickle.load(open('model/liver_final_model.pkl', 'rb'))
        input_data = (Age, sex, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase,
                        Total_Protiens, Albumin, Albumin_and_Globulin_Ratio)

        print(input_data)

        input_data_as_numpy_array= np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        print(input_data_reshaped)

        prediction = model_liver.predict(input_data_reshaped)
        print(prediction)
        senddata=""
        if (prediction[0]==2):
            predi="No Liver Disease"
            senddata='According to the given details person does not have any Liver Diesease.'
        else:
            predi="Liver Disease"
            senddata='According to the given details chances of having Liver Diesease are High, So Please Consult a Doctor'

        new_data = Liver(Age=Age, sex=gender, Total_Bilirubin=Total_Bilirubin, Direct_Bilirubin=Direct_Bilirubin,
                 Alkaline_Phosphotase=Alkaline_Phosphotase, Alamine_Aminotransferase=Alamine_Aminotransferase,
                  Aspartate_Aminotransferase=Aspartate_Aminotransferase,
                    Total_Protiens=Total_Protiens, Albumin=Albumin, Albumin_and_Globulin_Ratio=Albumin_and_Globulin_Ratio,
                        outcome=predi,
                        user_id=current_user.id)
        db.session.add(new_data)
        db.session.commit()

        return render_template('liver_pred.html', prediction_text=senddata)

@views.route('/liver_history')
@login_required
def liver_history():
    return render_template('liver_history.html', user=current_user)


# ------------------------------ Deep Learning --------------------------- #
# Model saved with Keras model.save()
# MODEL_PATH ='model/model_vgg19.h5'

# # Load your trained model
# model = load_model(MODEL_PATH)

# def model_predict(img_path, model):
#     img = image.load_img(img_path, target_size=(224, 224))

#     # Preprocessing the image
#     x = image.img_to_array(img)
#     # x = np.true_divide(x, 255)
#     ## Scaling
#     x=x/255
#     x = np.expand_dims(x, axis=0)

#     x = preprocess_input(x)

#     preds = model.predict(x)
#     print(preds)
#     preds=np.argmax(preds, axis=1)
#     print()

#     if preds==0:
#         preds="The Person is Infected With Malaria"
#     else:
#         preds="The Person is not Infected With Malaria"
#     return preds

# @views.route('/malaria', methods=['GET'])
# @login_required
# def malaria():
#     return render_template('malaria.html')

# @views.route('/malaria_pred', methods=['GET', 'POST'])
# @login_required
# def upload():
#     if request.method == 'POST':
#         # Get the file from post request
#         f = request.files['file']

#         # Save the file to ./uploads
#         basepath = os.path.dirname(__file__)
#         file_path = os.path.join(
#             basepath, 'uploads', secure_filename(f.filename))
#         f.save(file_path)

#         # Make prediction
#         preds = model_predict(file_path, model)
#         result=preds
#         return result
#     return None

# Malaria
@views.route("/malaria", methods=['GET', 'POST'])
@login_required
def malariaPage():
    return render_template('malaria_new.html')

@views.route("/malariapredict", methods = ['POST', 'GET'])
@login_required
def malariapredictPage():
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image'])
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,3))
                img = img.astype(np.float64)
                model = load_model("model/malaria.h5")
                pred = np.argmax(model.predict(img)[0])
                print(pred)
        except:
            message = "Please upload an Image"
            return render_template('malaria_new.html', message = message)
        return render_template('malaria_predict.html', pred = pred)
    else:
        return render_template('malaria_predict.html')


@views.route("/pneumonia", methods=['GET', 'POST'])
def pneumoniaPage():
    return render_template('pneumonia.html')

@views.route("/pneumoniapredict", methods = ['POST', 'GET'])
def pneumoniapredictPage():
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,1))
                img = img / 255.0
                model = load_model("model/pneumonia.h5")
                pred = np.argmax(model.predict(img)[0])
                print(pred)
        except:
            message = "Please upload an Image"
            return render_template('pneumonia.html', message = message)
        return render_template('pneumonia_predict.html', pred = pred)
    else:
        return render_template('pneumonia_predict.html')