# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/setter/product_setter.py
# Last Modified  : 02/06/21, 13:21 PM
# Copyright © Relarizky 2021


from app import apps
from help.exception import ValueLengthError, ValueFormatError
from help.app.uploader import FileUploader
from werkzeug.datastructures import FileStorage


class ProductSetter(FileUploader):
    """
    contains setter for Product (tb_product) with validation
    """

    def set_name(self, name: str) -> None:
        """
        set product name
        """

        if name.__len__() > 40:
            raise ValueLengthError("nama produk tidak bisa lebih dari 40")

        self.name = name

    def set_price(self, price: int) -> None:
        """
        set product price
        """

        if not price.isdigit():
            raise ValueFormatError("harga harus dalam bentuk angka")

        self.price = int(price)

    def set_status(self, status: str) -> None:
        """
        set product status
        """

        self.ready = bool(status)

    def set_picture(self, picture: FileStorage) -> None:
        """
        set product picture
        """

        file_name = self.upload_file(
            picture,
            apps.config.get("PRODUCT_IMAGE_DIR")
        )

        if file_name is not None:
            self.picture = file_name
