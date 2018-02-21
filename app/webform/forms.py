from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, ValidationError, IPAddress

from db_utils import *


def check_user_unique(form, username):
    if username.data in user_credentials:
        raise ValidationError('User exists')

def check_user_exists(form, username):
    if username.data not in user_credentials:
        raise ValidationError('User doesn\'t exist')

def check_password(form, password):
    if password.data != user_credentials[form.name.data]:
        raise ValidationError('Wrong password')


class SignUpForm(FlaskForm):
    name = TextField('name', validators=[Required(), check_user_unique])
    email = TextField('email', validators=[Required(), Email(message='Wrong email format')])
    password = PasswordField('password', validators=[Required()])


class LoginForm(FlaskForm):
    name = TextField('name', validators=[Required(), check_user_exists])
    password = PasswordField('password', validators=[Required(), lambda f,p: check_password(f, p)])

class AddServiceForm(FlaskForm):
    ip = TextField('ip', validators=[Required(), IPAddress(ipv4=True, message='Please input valid IP')])

