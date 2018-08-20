from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  #object that represents the database
migrate = Migrate(app, db) #object that represents the migration engine
login = LoginManager(app)

from app import routes, models
#the module module will define the structure of our database
