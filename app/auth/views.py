from ..import db,bcrypt
# from flask_bcrypt import Bcrypt
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from . import auth




@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('main.index')
    form  = RegisterForm()
    if form.validate_on_submit():
        
        try:
            username = form.username.data
            email = form.email.data
            pwd = form.pwd.data
                              
            
            user = User(username = username, email=email, pwd=pwd)
            
            db.session.add(user)
            db.session.commit()



            flash (f'Account Successfully Created!! Welcome')
            return redirect(url_for('auth/login'))
        except Exception as e:
            flash(e, "danger")

    return render_template('auth/register.html', form = form)


@auth.route('/login', methods=["GET", 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()

            if user is not None and user.pwd == form.pwd.data:

                
            # if check_password_hash(user.password, form.password.data):
                login_user(user, form.remember_me.data)
            else:
                flash("Invalid username or Password")
        except Exception as e:
            flash(e, "danger")


    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
