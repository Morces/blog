from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,Length, EqualTo, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    email = StringField('Your Email Address', validators=[InputRequired(),Email()])
    username = StringField('Enter your username', validators=[InputRequired()])
    pwd = PasswordField('Password', validators=[InputRequired(),Length(8, 72),EqualTo('password_confirm', message='Passwords do not match')])
    password_confirm  = PasswordField('Confirm Passwords',validators=[InputRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist!')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email already exixsts!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    pwd  = PasswordField('Password', validators=[InputRequired(), Length(8, 72)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')