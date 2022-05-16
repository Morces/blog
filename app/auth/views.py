from ..import db,bcrypt
# from flask_bcrypt import bcrypt
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app.auth.forms import LoginForm, RegisterForm
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


@auth.route('/login', methods=["GET", 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hush, form.password.data):
            login_user(user, remember=form.remember_me.data)
            
            return redirect(url_for('main.account'))
        flash ('Invalid username or Password!')

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')
