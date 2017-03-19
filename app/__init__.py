from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from app import views, models

db = SQLAlchemy(app)

# Support for login:

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'
