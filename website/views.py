from crypt import methods
from unicodedata import category
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from .models import Post, User
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
    post = Post.query.filter_by(id=id).first() #To check by ID if the post exists

    if not post:
        flash('Blog does not exist', category='error')
    elif current_user.id != post.id:
        flash('You do not have permission to delete this blog', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Blog deleted. Think twice!!', category = "success")
    return redirect(url_for('views.home'))

@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first() # To check if the username that the user typed actually exists.
    
    if not user:
        flash('No user with such a username in bloggit!!', category='error')
        return redirect(url_for('views.home'))
        
    post = Post.query.filter_by(username=username).all() # To get blogs by a certain user
    return render_template("posts.html", user=current_user, posts=posts)