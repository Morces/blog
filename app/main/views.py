from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app.main.forms import WriteForm

from . import main,db
from app.models import Posts


main.route('/')
def index():
    posts = Posts.query.all()

    return render_template('index.html',posts=posts)

@main.route('/publish/new', methods = ['GET', 'POST'])
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


