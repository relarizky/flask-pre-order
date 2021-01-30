# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/token.py
# Last Modified  : 01/30/21, 14:00 PM
# Copyright © Relarizky 2021


from app import apps
from jwt import encode, decode
from jwt.exceptions import ExpiredSignatureError, DecodeError
from typing import Union
from datetime import datetime, timedelta


def create_token(id_user: str, email: str) -> bytes:
    """
    create jwt token
    """

    token_data = {"id": id_user, "email": email}
    token_algorithm = apps.config.get("JWT_ALGORITHM")
    token_secret_key = apps.config.get("JWT_SECRET_KEY")
    token_expiration = datetime.utcnow() + timedelta(minutes=10)

    return encode(
        {"data": token_data, "exp": token_expiration},
        token_secret_key,
        algorithm=token_algorithm
    )


def confirm_token(token: str) -> Union[dict, None]:
    """
    decode and confirm jwt token
    """

    try:
        token_algorithm = apps.config.get("JWT_ALGORITHM")
        token_secret_key = apps.config.get("JWT_SECRET_KEY")
        token_decoded = decode(
            token,
            token_secret_key,
            algorithm=token_algorithm
        )
    except (ExpiredSignatureError, DecodeError):
        return None
    else:
        return token_decoded
