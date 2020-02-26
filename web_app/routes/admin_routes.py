from flask import Blueprint, jsonify
from web_app.models import db

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/reset")
def reset_db():
    db.drop_all()
    db.create_all()
    return jsonify({"message":"DB RESET OK"})
