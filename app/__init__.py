# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/__init__.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# create flask instance
apps = Flask(__name__)
apps.config.from_pyfile("configuration.py")


# create additional library instance
sql = SQLAlchemy(apps)
csrf = CSRFProtect(apps)
login = LoginManager(apps)
migrate = Migrate(apps, sql)


# import required modules
import app.model
import app.filter
import app.register
