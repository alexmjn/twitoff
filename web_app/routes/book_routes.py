from flask import Blueprint, jsonify, request, render_template, flash

from web_app.models import db, Book

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 13, "title": "Book 3"}
    ]
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 13, "title": "Book 3"}
    ]
    return render_template("books.html", message="Here's some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])
    db.session.add()
    db.session.commit()
    return jsonify({
        "message": "Book created OK",
        "book": dict(request.form)
        })
