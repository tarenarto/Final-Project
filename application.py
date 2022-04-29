import os
import requests
from urllib import request


from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
from sqlalchemy import create_engine, true
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registration", methods=["POST"])
def registration():
    username=request.form.get("username")
    password=request.form.get("password")

    if db.execute("SELECT * FROM users WHERE username=:username", {"username":username}).rowcount==1:
        return render_template("error.html", message="Username is already taken.")
    db.execute("INSERT INTO users (username, passwrd) VALUES (:username, :passwrd)", {"username":username, "passwrd":password})
    db.commit()
    return render_template("success.html")

@app.route("/loginform")
def loginform():
    return render_template('loginform.html')

@app.route("/login", methods=["POST"])
def login():
    username=request.form.get("username")
    password=request.form.get("password")

    if db.execute("SELECT * FROM users WHERE username=:username AND passwrd=:password" , {"username":username, "password":password}).rowcount==0:
        return render_template("error.html", message="Account does not exist.")

    user=db.execute("SELECT * FROM users WHERE username=:username AND passwrd=:password" , {"username":username, "password":password}).fetchone()

    session["userid"]=user["userid"]
    session["logged_in"]=True

    return render_template("APImap.html")
    
    
# @app.route("/booksearch", methods=["POST"])
# def booksearch():
#     search=request.form.get("search")
#     search_option=request.form.get("search_option")

#     if db.execute("SELECT * FROM books WHERE {} LIKE :search".format(search_option), {"search":'%'+search+'%'}).rowcount==0:
#         return render_template("error.html", message="Book does not exist")
    
#     books=db.execute("SELECT * FROM books WHERE {} LIKE :search".format(search_option), {"search":'%'+search+'%'}).fetchall()
#     return render_template("Bookslist.html",books=books)

# @app.route("/bookslist/<string:book_isbn>")
# def book(book_isbn):
    
#     res = requests.get("https://www.googleapis.com/books/v1/volumes", params={"q": "isbn:{}".format(book_isbn)})
#     data=res.json()
    
#     book=db.execute("SELECT * FROM books WHERE isbn=:isbn", {"isbn":book_isbn}).fetchone()
#     if book is None:
#         return render_template("error.html", message="No such book.")

#     book=db.execute("SELECT * FROM books WHERE isbn=:isbn", {"isbn":book_isbn}).fetchone()
#     review_count=db.execute("SELECT COUNT(*) FROM reviews WHERE isbn=:isbn", {"isbn":book_isbn}).fetchone()
#     reviews=db.execute("SELECT * FROM reviews WHERE isbn=:isbn", {"isbn":book_isbn}).fetchall()
#     return render_template("book.html", book=book, reviews=reviews, review_count=review_count, data=data)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("userid", None)
    return render_template("loginform.html")

# @app.route("/bookslist/<string:book_isbn>/reviews", methods=["POST"])
# def reviews(book_isbn):
#     rating=request.form.get("rating")
#     review_description=request.form.get("review_description")

#     # listing out reviews
#     review=db.execute("SELECT * FROM reviews WHERE isbn=:isbn ", {"isbn":book_isbn, "userid":session["userid"]}).fetchall()

#     # check if user can submit review
#     if db.execute("SELECT * FROM reviews WHERE isbn=:isbn AND userid=:userid", {"isbn":book_isbn, "userid":session["userid"]}).rowcount==1:
#         return render_template("error.html", message="You can only submit one review for a book.")

#     #submitting review
#     db.execute("INSERT INTO reviews (rating, description, isbn, userid) VALUES (:rating, :review_description, :isbn, :userid)", {"rating":rating, "review_description":review_description, "isbn":book_isbn, "userid":session["userid"]})
#     db.commit()
    
#     book=db.execute("SELECT * FROM books WHERE isbn=:isbn", {"isbn":book_isbn}).fetchone()
#     review_count=db.execute("SELECT COUNT(*) FROM reviews WHERE isbn=:isbn", {"isbn":book_isbn}).fetchone()
#     reviews=db.execute("SELECT * FROM reviews WHERE isbn=:isbn", {"isbn":book_isbn}).fetchall()
#     return render_template("book.html", book=book, reviews=reviews, review_count=review_count)
    
# @app.route("/api/<string:book_isbn>")
# def api(book_isbn):
#     res = requests.get("https://www.googleapis.com/books/v1/volumes", params={"q": "isbn:{}".format(book_isbn)})

#     data=res.json()
#     return (data)

    

