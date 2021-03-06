import os
import secrets
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app.main.forms import EditProfile, WriteForm
from app.models import Posts, User
from app.requests import get_quotes
from .. import db
from . import main


@main.route('/')
def index():
    posts = Posts.query.all()

    return render_template('index.html', posts=posts)

@main.route('/new', methods = ['GET', 'POST'])
@login_required
def write():
    form = WriteForm()

    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.story.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('You have created a post successfully!')
        return redirect(url_for('main.account'))

    posts = Posts.query.all()
    return render_template('write.html', form = form, posts=posts)

@main.route('/account')
@login_required
def account():
    quotes = get_quotes()
    posts = Posts.query.all()
    image = current_user.image_url
    return render_template('account.html', quotes=quotes, posts=posts,image=image)

def save_pic(form_picture):
    random_hex = secrets.token_hex(8)
    fn_ext = os.path.splitext(form_picture.filename)
    picture_fn = fn_ext
    pic_full_path = os.path.join('app/static/img')
    form_picture.save(pic_full_path)
    return picture_fn


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = EditProfile()
    image_file = url_for('static', filename='img'+'')
    posts = Posts.query.all()
    user = User.query.filter_by(username=current_user.username).first
    if form.validate_on_submit():
        if form.picture_upload.data:
            picture_file = save_pic(form.picture_upload.data)
            current_user.image_url = picture_file
            current_user.username = form.user.data
            current_user.bio = form.bio.data
            db.session.add()
            db.session.commit()
            flash('Account updated Successfully!')
    form.user.data = current_user.username
    form.bio.data = current_user.bio

    return render_template('userprof.html', form=form, image=image_file, user=user, posts=posts)

@main.route('/post/<post_id>')
def post(post_id):
    posts = Posts.query.get_or_404(post_id)

    return render_template('post.html', posts = posts)

@main.route('/post/<post_id>/delete')
def delete(post_id):
    post  = Posts.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.account'))


