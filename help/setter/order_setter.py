# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/setter/order_setter.py
# Last Modified  : 02/09/21, 22:37 PM
# Copyright © Relarizky 2021


from app import apps
from help.exception import ValueFormatError
from help.app.uploader import FileUploader
from werkzeug.datastructures import FileStorage


class OrderSetter(FileUploader):
    """
    contains setter for Order (tb_order) with validation
    """

    def set_pieces(self, pieces: int) -> None:
        """
        set pieces
        """

        if not pieces.isdigit():
            raise ValueFormatError("jumlah harus berupa angka")

        self.pieces = pieces

    def set_address(self, address: str) -> None:
        """
        set address
        """

        self.address = address

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
