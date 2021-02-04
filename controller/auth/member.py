# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/auth/member.py
# Last Modified  : 01/30/21, 14:00 PM
# Copyright © Relarizky 2021


from app.model import Member
from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_user, logout_user, login_required
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from controller.auth.auth import auth_bp

from help.token import create_token, confirm_token
from help.app.auth import member_required, member_unrequired, token_required
from help.app.email import EmailConfirmation
from help.app.blueprint import NestedBlueprint


member_auth_bp = NestedBlueprint(auth_bp, "/member")


@member_auth_bp.route("/")
@member_auth_bp.route("/login")
@member_unrequired
def login_member():
    """
    represents member login page
    """

    return render_template("auth/member/login.html")


@member_auth_bp.route("/register")
@member_unrequired
def register_member():
    """
    represents member register page
    """

    return render_template("auth/member/register.html")


@member_auth_bp.route("/forgot")
@member_unrequired
def forgot_password():
    """
    represents member forgot password page
    """

    return render_template("auth/member/forgot.html")


@member_auth_bp.route("/forgot/password/<token>")
@member_unrequired
@token_required
def change_password(token: str):
    """
    represents member change password page
    """

    session["token"] = token

    return render_template("auth/member/password.html")


@member_auth_bp.route("/login/process", methods=["POST"])
@member_unrequired
def login_member_process():
    """
    represents member login processing url
    """

    user_name = request.form.get("user_name")
    pass_word = request.form.get("pass_word")
    remember_me = request.form.get("remember_me")
    member = Member.query.filter_by(user_name=user_name).first()

    if (member is not None) and member.check_password(pass_word):
        # user is valid
        session.clear()
        session["is_member"] = True
        flash("success", f"Selamat datang, {member.user_name.capitalize()}")
        login_user(user=member, remember=bool(remember_me))
    else:
        flash("error", "username atau password anda salah")

    return redirect(url_for("auth.login_member"))


@member_auth_bp.route("/register/process", methods=["POST"])
@member_unrequired
def register_member_process():
    """
    represents member register processing url
    """

    real_name = request.form.get("real_name")
    user_name = request.form.get("user_name")
    pass_word = request.form.get("pass_word")
    email = request.form.get("email")
    phone = request.form.get("phone")

    try:
        new_member = Member(
            real_name,
            user_name,
            pass_word,
            phone,
            email
        )
        new_member.save()
    except IntegrityError:
        flash("error", "credentials yang anda masukan duplicated")
        return redirect(url_for("auth.register_member"))
    except Exception as Error:
        flash("error", Error.__str__())
        return redirect(url_for("auth.register_member"))

    # send registration confirmation mail
    email_sender = EmailConfirmation.register_confirmation(
        new_member.email,
        url_for(
            "auth.register_confirmation_token",
            token=create_token(new_member.id, new_member.email),
            _external=True
        )
    )
    email_sender.send_mail()

    # create session
    session.clear()
    session["is_member"] = True
    login_user(user=new_member)

    flash("success", "Berhasil registrasi, silahkan cek email anda")
    return redirect(url_for("index.index"))


@member_auth_bp.route("/forgot/process", methods=["POST"])
@member_unrequired
def forgot_password_process():
    """
    represents forgot password processing url
    """

    user_identifier = request.form.get("identifier")
    user_object = Member.query.filter(
        or_(
            Member.email == user_identifier,
            Member.user_name == user_identifier
        )
    ).first()

    if user_object is None:
        # can't find user with given identifier
        flash("error", "username / email tidak ada...")
        return redirect(url_for("auth.forgot_password"))

    # send email
    email = EmailConfirmation.forgot_password_confirmation(
        user_object.email,
        url_for(
            "auth.change_password",
            token=create_token(user_object.id, user_object.email),
            _external=True
        )
    )
    email.send_mail()

    flash("success", "silahkan cek email anda untuk konfirmasi")
    return redirect(url_for("auth.login_member"))


@member_auth_bp.route("/forgot/password/process", methods=["POST"])
@member_unrequired
@token_required
def change_password_process():
    """
    represents change password processing url
    """

    pass_word = request.form.get("pass_word")
    repeat_pass_word = request.form.get("repeat_pass_word")
    user_token = confirm_token(session.get("token"))

    if pass_word != repeat_pass_word:
        # password does not match
        flash("error", "password tidak cocok")
        return redirect(
            url_for(
                "auth.change_password",
                token=session.get("token")
            )
        )

    try:
        user_object = Member.query.get(user_token["data"]["id"])
        user_object.set_pass_word(pass_word)
        user_object.save()
    except Exception as Error:
        flash("error", Error.__str__())
        return redirect(
            url_for(
                "auth.change_password",
                token=session.get("token")
            )
        )
    else:
        flash("success", "berhasil mengubah password")

    return redirect(url_for("auth.login_member"))


@member_auth_bp.route("/register/confirm/<token>")
@login_required
@member_required
def register_confirmation_token(token: str):
    """
    represents member register confirmation url
    """

    user_token = confirm_token(token)

    if user_token is None:
        flash("error", "token sudah expired atau tidak valid")
        return redirect(url_for("index.index"))

    user_objek = Member.query.get(user_token["data"]["id"])

    if user_objek.verified:
        flash("error", "akun sudah verified")
    else:
        user_objek.verified = True
        user_objek.save()
        flash("success", "berhasil verifikasi akun")

    return redirect(url_for("index.index"))


@member_auth_bp.route("/logout")
@login_required
@member_required
def logout_member():
    """
    represents member logout url
    """

    logout_user()
    session.clear()

    return redirect(url_for("index.index"))
