# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/configuration.py
# Last Modified  : 01/24/21, 04:28 PM
# Copyright © Relarizky 2021


from os import environ


# Flask App Configuration
SECRET_KEY = environ.get("SECRET_KEY")


# MySQL Credentials
HOST_NAME = environ.get("HOST_NAME")
USER_NAME = environ.get("USER_NAME")
PASS_WORD = environ.get("PASS_WORD")
DATA_BASE = environ.get("DATA_BASE")


# SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URI = f"mysql://{USER_NAME}:{PASS_WORD}@{HOST_NAME}/{DATA_BASE}"
SQLALCHEMY_TRACK_MODIFICATIONS = True
