from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import InputRequired, ValidationError
from flask_wtf.file import FileAllowed, FileField

from app.models import User

class WriteForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    story = StringField('Write something', validators=[InputRequired()])
    submit = SubmitField('Publish')

class EditProfile(FlaskForm):
    user = StringField('Username')
    bio = TextAreaField('Add more about yourself')
    picture_upload = FileField('Upload profile picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    def username(self, field):
        if field.data != current_user.user:
            user = User.query.filter_by(username = field.data)
            if user:
                raise ValidationError('Username already exists!')