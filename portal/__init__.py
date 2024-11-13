# python packages execute init file when pkg is loaded

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

# refers to local python file you are working in
app = Flask(__name__)

# classes (models) can be converted into db tables
# file will be identified as a db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SECRET_KEY'] = '3330f7af302dfff543a79988'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# store passworsd as hash in db
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
# redirects users to login page when trying to visit a page that requires authentrification
login_manager.login_view="login_page"
login_manager.login_message_category="info"
login_manager.init_app(app) #lets routes use current_user
# must come at end or causes circular imports with importing app in run.py
from portal import routes, models