# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/configuration.py
# Last Modified  : 01/30/21, 14:00 PM
# Copyright © Relarizky 2021


from os import environ, getcwd


# Flask App Configuration
DEBUG = True  # change it to false in production env
SECRET_KEY = environ.get("SECRET_KEY")
FLASK_DBMS = environ.get("FLASK_DBMS").lower()
PROOF_IMAGE_DIR = getcwd() + "/asset/picture/proof/"
PRODUCT_IMAGE_DIR = getcwd() + "/asset/picture/product/"


# JWT Token Configuration
JWT_ALGORITHM = "HS256"  # https://pyjwt.readthedocs.io/en/stable/algorithms.html for more
JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")


# Mail Configuration
MAIL_SERVER = "smtp.gmail.com"  # use google smtp server by default
MAIL_PORT = 465  # port for using SSL
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = environ.get("MAIL_USERNAME")
MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = environ.get("MAIL_USERNAME")


# MySQL Credentials
HOST_NAME = environ.get("HOST_NAME")
USER_NAME = environ.get("USER_NAME")
PASS_WORD = environ.get("PASS_WORD")
DATA_BASE = environ.get("DATA_BASE")
MYSQL = f"mysql://{USER_NAME}:{PASS_WORD}@{HOST_NAME}/{DATA_BASE}"


# SQLite Credentials
FILE_NAME = environ.get("FILE_NAME")
SQLITE = f"sqlite:///{FILE_NAME}"


# SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URI = MYSQL if FLASK_DBMS == "mysql" else SQLITE
SQLALCHEMY_TRACK_MODIFICATIONS = True
