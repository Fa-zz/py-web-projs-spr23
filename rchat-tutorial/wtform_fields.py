from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    """ Registration form has 3 fields: username field, pw field, pw confirm field """

    username = StringField('username_label')
    password = PasswordField('password_label')
    confirm_pwd = PasswordField('confirm_pwd_label')