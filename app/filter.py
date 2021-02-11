# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/filter.py
# Last Modified  : 02/11/21, 23:51 PM
# Copyright © Relarizky 2021


from os import getcwd
from app import apps
import locale


@apps.template_filter("pascal_case")
def pascal_case(text: str) -> str:
    """
    convert given text into pascal case
    """

    text = text.split()
    text = map(lambda string: string.capitalize(), text)

    return " ".join(text)


@apps.template_filter("product_pict")
def product_pict(image: str) -> str:
    """
    add path into product picture
    """

    pict_dir = apps.config.get("PRODUCT_IMAGE_DIR").replace(getcwd(), "")
    pict_name = pict_dir + image

    return pict_name


@apps.template_filter("proof_pict")
def proof_pict(image: str) -> str:
    """
    add path into proof picture
    """

    pict_dir = apps.config.get("PROOF_IMAGE_DIR").replace(getcwd(), "")
    pict_name = pict_dir + image

    return pict_name


@apps.template_filter("rupiah")
def rupiah_format(number: int) -> str:
    """
    re-format integer into rupiah
    """

    locale.setlocale(locale.LC_NUMERIC, "")
    rupiah = locale.format("%.*f", (0, number), True)

    return rupiah
