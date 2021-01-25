# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/database.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from app import sql as db
from random import randint
from datetime import datetime
from help.hash import create_md5


class DBHelper:
    """
    contains method to simplify saving and deleting record from db
    """

    def save(self):
        """
        save changes into database
        """

        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        delete record from database
        """

        db.session.delete(self)
        db.session.commit()


def create_uuid():
    """
    create random unique identifier
    """

    time = datetime.now()
    text = f"{time.year}{time.month}{time.hour}{time.minute}{time.second}"
    text += str(randint(1, 100000))

    return create_md5(text)[:5].upper()
