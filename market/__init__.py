# python packages execute init file when pkg is loaded

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# refers to local python file you are working in
app = Flask(__name__)

# classes (models) can be converted into db tables
# file will be identified as a db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '3330f7af302dfff543a79988'
db = SQLAlchemy(app)

# store passworsd as hash in db
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

# must come at end or causes circular imports with importing app in run.py
from market import routes
from market import models