# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/exception.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


class ValueLengthError(Exception):
    """
    raised when user input value with invalid length
    """

    def __init__(self, message: str) -> None:
        self.message = message


class ValueFormatError(Exception):
    """
    raised when user input value with invalid format
    """

    def __init__(self, message: str) -> None:
        self.message = message


class ObjectDoesNotExist(Exception):
    """
    raised when user try to access unexisting object
    """

    def __init__(self, message: str) -> None:
        self.message = message
