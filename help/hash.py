# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/hash.py
# Last Modified  : 01/25/21, 11:23 PM
# Copyright © Relarizky 2021


from hashlib import md5, sha224


def create_sha224(plain_text: str) -> str:
    """
    create sha1 hash
    """

    return sha224(plain_text.encode("utf-8")).hexdigest()


def create_md5(plain_text: str) -> str:
    """
    create md5 hash
    """

    return md5(plain_text.encode("utf-8")).hexdigest()
