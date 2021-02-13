# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/__init__.py
# Last Modified  : 02/13/21, 21:18 PM
# Copyright © Relarizky 2021


import pymysql
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# create flask instance
apps = Flask(__name__, static_folder="../asset/")
apps.config.from_pyfile("configuration.py")


# create additional library instance
pymysql.install_as_MySQLdb()
api = Api(apps, prefix="/api")
sql = SQLAlchemy(apps)
mail = Mail(apps)
csrf = CSRFProtect(apps)
login = LoginManager(apps)
migrate = Migrate(apps, sql)


# import required modules
import app.model
import app.filter
import app.register
