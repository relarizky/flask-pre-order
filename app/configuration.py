# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/configuration.py
# Last Modified  : 01/24/21, 04:28 PM
# Copyright © Relarizky 2021


from os import environ, getcwd


# Flask App Configuration
SECRET_KEY = environ.get("SECRET_KEY")
FLASK_DBMS = environ.get("FLASK_DBMS").lower()
PROOF_IMAGE_DIR = getcwd() + "/route/index/asset/picture/proof/"
PRODUCT_IMAGE_DIR = getcwd() + "/route/index/asset/picture/product/"


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
