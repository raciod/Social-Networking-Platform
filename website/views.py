from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/projects")
def projects():
    return "<h1>Projects</h1>"

@views.route("/blog")
def blog():
    return "<h1>Blog</h1>"