from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C://Users//ajenk//GitHub//twitoff//twitoff.db"
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web_app_11.db"

#    db.init_app(app)
 #   migrate.init_app(app, db)



    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(128))
        author_id = db.Column(db.String(128))

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app
