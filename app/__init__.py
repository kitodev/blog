from flask import Flask
from app.forms import ContactForm
from flask_mail import Mail
# import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'tkornel19'
app.config["MAIL_PASSWORD"] = 'Jancsi18912323.1*'

app.config['SECRET_KEY'] = '8d5c6dc3a01b5e4e85474cf28243972681655216592491a8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
mail.init_app(app)

from app import routes
