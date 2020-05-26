from flask_wtf import Form, FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, PasswordField, BooleanField, StringField
from wtforms.validators import Required, ValidationError, DataRequired, Email, EqualTo, Length
# from app.models import User

class ContactForm(Form):
    name = TextField("Name", [validators.DataRequired("Enter your name")])
    email = TextField("Email", [validators.DataRequired("Enter your email"), validators.Email("Enter a valid email address")])
    message = TextAreaField("Message", [validators.DataRequired("Didn't you want to say something?")])
    subject = TextField("Subject", [validators.DataRequired("What's the nature of your message?")])
    submit = SubmitField("Send")


class RegistrationForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired("Enter your username"), Length(min=2, max=20)])
    email = StringField("Email", [validators.DataRequired("Enter your email")])
    password = PasswordField("Password", [validators.DataRequired("Enter your password")])
    confirm_password = PasswordField("Confirm Password",  [validators.DataRequired("Enter your password again"), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken')

class LoginForm(FlaskForm):
    email = StringField("Email", [validators.DataRequired("Enter your email"), Email()])
    password = PasswordField("Password", [validators.DataRequired("Enter your password")])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")

class PostForm(FlaskForm):
    title =  StringField('Title', [validators.DataRequired()])
    subtitle = StringField('Sub title', [validators.DataRequired()])
    content = TextAreaField('Content', [validators.DataRequired()])
    submit = SubmitField('Post')