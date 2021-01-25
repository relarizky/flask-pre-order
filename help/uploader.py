# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/uploader.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from os import getcwd
from app import apps
from typing import Union
from help.hash import create_md5
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


class FileUploader:
    """
    contains method as helper for uploading a file
    """

    @staticmethod
    def filter_extension(file_name: str) -> bool:
        """
        fileter file name extension
        """

        ext = file_name.split(".")[-1].lower()

        return ext in ("jpg", "png", "jpeg")

    @staticmethod
    def create_file_name(file_name: str) -> str:
        """
        create hash file name
        """


        file_name, file_ext = file_name.split(".")
        file_name = create_md5(file_name)

        return file_name + "." + file_ext.lower()

    def upload_file(self, file: FileStorage, dir: str) -> Union[None, str]:
        """
        upload file
        """

        file_name = file.filename

        if file_name.__len__() == 0:
            return

        if not self.filter_extension(file_name):
            return

        file_name = secure_filename(self.create_file_name(file_name))
        file.save(dir + file_name)

        return file_name
