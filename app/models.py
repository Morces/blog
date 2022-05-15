from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(), nullable = False)
    password = db.Column(db.String(80))



    @property
    def password(self):
        raise AttributeError('password is not a readable input')

    @password.setter
    def password(self,password):
        self.password_hush = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hush,password)

    def __repr__(self) -> str:
        return '<User %r>' % self.username



class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(20), nullable = False)
    content = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime(), index = True, default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __repr__(self):
        return 'User %r' %self.content

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    comment = db.Column(db.String(255), nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))