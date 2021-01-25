# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/setter/category_setter.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from help.exception import ValueLengthError


class CategorySetter:
    """
    contains setter for Category (tb_category) with validation
    """

    def set_name(self, name: str) -> None:
        """
        set category name
        """

        if name.__len__() > 20:
            raise ValueLengthError("nama kategori tidak boleh lebih dari 20")

        self.name = name
