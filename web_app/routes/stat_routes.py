
from flask import Blueprint, jsonify, request, render_template, flash

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

stat_routes = Blueprint("stat_routes", __name__)

@stat_routes.route('/iris')
def iris():
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)

    return str(clf.predict(X[:2, :]))
