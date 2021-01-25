# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/setter/order_setter.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from app import apps
from app.model import Member, Product
from help.uploader import FileUploader
from help.exception import ValueLengthError, ObjectDoesNotExist, ValueFormatError
from werkzeug.datastructures import FileStorage


class OrderSetter(FileUploader):
    """
    contains setter for Order (tb_order) with validation
    """

    def set_member(self, current_member: Member) -> None:
        """
        set member
        """

        self.member = current_member

    def set_product(self, product_id: str) -> None:
        """
        set product by its id
        """

        product = Product.query.get(product_id)

        if product is None:
            raise ObjectDoesNotExist("produk tidak ditemukan")

        self.product = product

    def set_pieces(self, pieces: int) -> None:
        """
        set pieces
        """

        if not pieces.isdigit():
            raise ValueFormatError("jumlah harus berupa angka")

        self.pieces = pieces

    def set_paid_off(self, paid_off: bool) -> None:
        """
        set paid off
        """

        self.paid_off = paid_off

    def set_payment_proof(self, picture: FileStorage) -> None:
        """
        set payment proof picture
        """

        file_name = self.upload_file(
            picture,
            apps.config.get("PROOF_IMAGE_DIR")
        )

        if file_name is None:
            raise ValueFormatError("ekstensi gambar tidak valid")

        self.payment_proof = file_name
