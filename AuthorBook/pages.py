from flask import Blueprint,  render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def index():
    # return 'Good Reads!'
    return render_template('pages/index.html')

@bp.route("/ebooks")
def ebooks():
    return render_template('pages/ebook.html')


@bp.route("/authors")
def get_authors():
    authors = ["Bob", "Tom", "Ann"]
    return authors

@bp.route("/books")
def get_books():
    books = ["The Hunger Games", "Harry Potter and the Order of the Phoenix", "Pride and Prejudice"]
    return books