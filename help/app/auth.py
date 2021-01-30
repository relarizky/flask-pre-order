# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/app/auth.py
# Last Modified  : 01/30/21, 14:00 PM
# Copyright © Relarizky 2021


from app import login
from flask import session, redirect, url_for, flash
from typing import Callable
from functools import wraps
from flask_login import current_user
from help.token import confirm_token


def admin_required(func: Callable) -> Callable:
    """
    prevent not admin user for accessing protected controller
    """
    @wraps(func)
    def validate(*args: list, **kwargs: dict):
        if not session.get("is_admin"):
            # not an admin, we need to throw it out:)
            return login.unauthorized()

        return func(*args, **kwargs)

    return validate


def member_required(func: Callable) -> Callable:
    """
    prevent not member user for accessing protected controller
    """
    @wraps(func)
    def validate(*args: list, **kwargs: dict):
        if not session.get("is_member"):
            # not a member, we need to throw it out:)
            return login.unauthorized()

        return func(*args, **kwargs)

    return validate


def admin_unrequired(func: Callable) -> Callable:
    """
    prevent authenticated admin to access admin login page
    """
    @wraps(func)
    def validate(*args: list, **kwargs: dict):
        if current_user.is_authenticated and session.get("is_admin"):
            # admin is authenticated, we need to redirect it to dashboard:)
            return redirect(url_for("dashboard.index"))

        return func(*args, **kwargs)

    return validate


def member_unrequired(func: Callable) -> Callable:
    """
    prevent authenticated member to access member login and register page
    """
    @wraps(func)
    def validate(*args: list, **kwargs: dict):
        if current_user.is_authenticated and session.get("is_member"):
            # member is authenticated, we need to redirect it to home page:)
            return redirect(url_for("index.index"))

        return func(*args, **kwargs)

    return validate


def verified_required(func: Callable) -> Callable:
    """
    prevent authenticated unverified user to access protected pages
    """
    @wraps(func)
    def validate(*args: list, **kwargs: dict):
        if session.get("is_member"):
            if not current_user.verified:
                # this authenticated isnt verified, we need to redirect it out
                return redirect(url_for("index.unverified"))

        return func(*args, **kwargs)

    return validate


def token_required(func: Callable) -> Callable:
    """
    check token in session
    """
    @wraps(func)
    def validate(*args: list, **kwargs: dict):
        token = kwargs.get("token") or session.get("token")
        token = confirm_token(token)

        if token is None:
            # invalid to decode token
            flash("error", "your token is invalid or expired")
            return redirect(url_for("auth.forgot_password"))

        return func(*args, **kwargs)

    return validate
