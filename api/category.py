# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : api/category.py
# Last Modified  : 02/06/21, 13:21 PM
# Copyright © Relarizky 2021


from app import api
from app.model import Category
from flask_restful import Resource


class CategoryAPI(Resource):
    """
    category API
    """

    def get(self):
        """
        GET method
        """

        categories = [
            [category.id, category.name] for category in Category.query.all()
        ]

        return categories
