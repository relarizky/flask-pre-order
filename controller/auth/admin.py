# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/auth/admin.py
# Last Modified  : 01/30/21, 14:00 PM
# Copyright © Relarizky 2021


from app.model import Admin
from flask import render_template, request, url_for, redirect, session, flash
from flask_login import login_user, logout_user, login_required
from help.app.auth import admin_required, admin_unrequired
from help.app.blueprint import NestedBlueprint
from controller.auth.auth import auth_bp


admin_auth_bp = NestedBlueprint(auth_bp, "/admin")


@admin_auth_bp.route("/")
@admin_unrequired
def login_admin():
    """
    represents admin login page
    """

    return render_template("auth/admin/login.html")


@admin_auth_bp.route("/process", methods=["POST"])
@admin_unrequired
def login_admin_process():
    """
    represents admin login processing url
    """

    user_name = request.form.get("user_name")
    pass_word = request.form.get("pass_word")
    remember_me = request.form.get("remember_me")
    admin = Admin.query.filter_by(user_name=user_name).first()

    if (admin is not None) and admin.check_password(pass_word):
        # user is valid
        session.clear()
        session["is_admin"] = True
        flash("success", f"Selamat datang, {admin.user_name.capitalize()}")
        login_user(user=admin, remember=bool(remember_me))
    else:
        flash("error", "username atau password anda salah")

    return redirect(url_for("auth.login_admin"))


@admin_auth_bp.route("/logout")
@login_required
@admin_required
def logout_admin():
    """
    represents admin logout url
    """

    logout_user()
    session.clear()

    return redirect(url_for("auth.login_admin"))
