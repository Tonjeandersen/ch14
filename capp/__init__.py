from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

### Code GitHub
application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
DBVAR=os.environ['DATABASE_URL']
# DBVAR="postgresql://username:os.environ.get(‘DB_PASSWORD’)@host:port/database"
# DBVAR="postgresql://username:password@host:port/database"
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
# application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

### Code computer
#DBVAR="postgresql://pssasqtwhdaqih:3cb955b66439692892ac9c9de78d79ca578e37f0ec82373e82aa6cf52fa0d26b@ec2-34-242-154-118.eu-west-1.compute.amazonaws.com:5432/dbe1is97pj69kk"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

