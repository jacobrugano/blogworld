from crypt import methods
from unicodedata import category
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Blog area can not be empty!!', category="error")
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Blog successfully created!!', category="success")
            return redirect(url_for('views.home'))

    return render_template("create_post.html", user=current_user)

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash('Blog does not exist', cateory='error')
    elif current_user.id != post.id:
        flash('You do not have permission to delete this blog')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Blog deleted!!', category = "success")