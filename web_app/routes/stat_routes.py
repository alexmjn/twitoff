
from flask import Blueprint, jsonify, request, render_template, flash

#request lets us get stuff from the html form along with methods
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from web_app.models import User, Tweet, db
from web_app.basilica_service import connection as basilica_api_client
from web_app.predict import predict
import numpy as np

stat_routes = Blueprint("stat_routes", __name__)

@stat_routes.route('/iris')
def iris():
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)

    return str(clf.predict(X[:2, :]))

@stat_routes.route("/predict", methods=["POST"])
def run_predict():
    return predict()
