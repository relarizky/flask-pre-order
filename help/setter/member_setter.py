# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/setter/member_setter.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from re import search
from help.hash import create_sha224
from help.exception import ValueLengthError, ValueFormatError


class MemberSetter:
    """
    contains setter for Member (tb_member) with validation
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

    def set_phone_number(self, phone: str) -> None:
        """
        set phone number
        """

        if not self.validate_phone_number(phone):
            raise ValueFormatError("nomor handphone tidak valid")

        self.phone = phone

    def set_email_address(self, email: str) -> None:
        """
        set email address
        """

        if not self.validate_email_address(email):
            raise ValueFormatError("email tidak valid")

        if email.__len__() > 40:
            raise ValueLengthError("email tidak boleh lebih dari 40")

        self.email = email

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """
        validate phone number
        """

        format = search(r"[0-9]{12}", phone)

        return format is not None

    @staticmethod
    def validate_email_address(email: str) -> bool:
        """
        validate email format
        """

        format = search(r"[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-z]{2,3}", email)

        return format is not None
