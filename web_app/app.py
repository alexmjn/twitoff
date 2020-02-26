from flask import Flask, jsonify, render_template, request
# pylint: disable=import-error
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.admin_routes import admin_routes
from web_app.routes.stat_routes import stat_routes

def create_app():

    app = Flask(__name__)
#adding the fourth slash made it not run
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C://Users//ajenk//GitHub//twitoff//twitoff.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web_app_11.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 #   app.config["SECRET_KEY"] = SECRET_KEY

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(stat_routes)

    return app
