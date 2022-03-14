from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html", name="Jacob", age = "34", school = "MOringa", status = "Married")