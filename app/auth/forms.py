from email import message
from click import confirm
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Enter your email', validators=[InputRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('Confirm_password', message='Passwords do not match')])
    submit = SubmitField('Register')