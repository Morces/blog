from ..import db
from flask_bcrypt import bcrypt
from flask import redirect, render_template, url_for
from flask_login import current_user

from app.auth.forms import RegisterForm
from app.models import User
from . import auth




@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('main.index')
    form  = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth/login'))

    return render_template('auth/register.html', form = form)
