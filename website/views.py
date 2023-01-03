# Here i will be storing the routes(location) of my website visible to the user

from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Diabetes
from . import db
import json


views = Blueprint('views', __name__)

@views.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home2.html")