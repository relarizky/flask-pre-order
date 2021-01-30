# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/app/blueprint.py
# Last Modified  : 01/27/21, 21:58 PM
# Copyright © Relarizky 2021


from flask import Blueprint


class NestedBlueprint:
    """
    create nested blueprint
    """

    def __init__(self, blueprint: Blueprint, url_prefix: str):
        self.blueprint = blueprint
        self.url_prefix = url_prefix

    def route(self, route: str, **options: dict) -> None:
        """
        create nested route
        """

        nested_route = self.url_prefix + route

        return self.blueprint.route(nested_route, **options)
