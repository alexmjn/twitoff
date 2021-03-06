from flask import Blueprint, jsonify, request, render_template, flash

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("home.html")

@home_routes.route("/about")
def about():
    return "About me"
