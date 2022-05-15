from flask import render_template

from app import main
from app.models import Posts


main.route('/')
def index():
    posts = Posts.query.all()

    return render_template('index.html',posts=posts)

