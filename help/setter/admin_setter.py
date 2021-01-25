# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/setter/admin_setter.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from help.hash import create_sha224
from help.exception import ValueLengthError


class AdminSetter:
    """
    contains setter for Admin (tb_admin) with validation
    """

    def set_real_name(self, real_name: str) -> None:
        """
        set real name
        """

        if real_name.__len__() > 40:
            raise ValueLengthError("real name tidak boleh lebih dari 40")

        self.real_name = real_name

    def set_user_name(self, user_name: str) -> None:
        """
        set user name
        """

        if user_name.__len__() > 20:
            raise ValueLengthError("user name tidak boleh lebih dari 20")

        self.user_name = user_name

    def set_pass_word(self, pass_word: str) -> None:
        """
        set pass word
        """

        if pass_word.__len__() < 8:
            raise ValueLengthError("pass word harus lebih dari 8")

        self.pass_word = create_sha224(pass_word)
