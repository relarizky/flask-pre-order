# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/auth/auth.py
# Last Modified  : 01/30/21, 14:00 PM
# Copyright © Relarizky 2021


from app import login
from app.model import Admin, Member
from flask import Blueprint, session
from typing import Union


auth_bp = Blueprint(
    "auth",
    __name__,
    template_folder="view/"
)


@login.user_loader
def load_user(id: str) -> Union[Admin, Member, None]:
    """
    load user by its id for all pages
    """

    if not ("is_admin" in session or "is_member" in session):
        # anonymous user (user that has not been logged in)
        return None

    if "is_member" in session:
        return Member.query.get(id)

    return Admin.query.get(id)


import controller.auth.admin
import controller.auth.member
