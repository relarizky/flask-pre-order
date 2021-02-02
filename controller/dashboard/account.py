# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/dashboard/account.py
# Last Modified  : 02/02/21, 03:20 PM
# Copyright © Relarizky 2021


from flask import render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from help.app.auth import admin_required
from help.app.blueprint import NestedBlueprint
from controller.dashboard.dashboard import dashboard_bp
from sqlalchemy.exc import IntegrityError
from app.model import Admin, Member


dashboard_account_bp = NestedBlueprint(
    dashboard_bp,
    "/account"
)

@dashboard_account_bp.route("/admin")
@login_required
@admin_required
def admin():
    """
    represents admin account list page
    """

    admin_list = Admin.query.all()

    return render_template(
        "dashboard/account/admin.html",
        user_list=admin_list
    )


@dashboard_account_bp.route("/member")
@login_required
@admin_required
def member():
    """
    represents member account list page
    """

    member_list = Member.query.all()

    return render_template(
        "dashboard/account/member.html",
        user_list=member_list
    )


@dashboard_account_bp.route("/admin/add", methods=["POST"])
@login_required
@admin_required
def admin_add():
    """
    represents admin account add processing url
    """

    real_name = request.form.get("real_name")
    user_name = request.form.get("user_name")
    pass_word = request.form.get("pass_word")

    try:
        new_admin = Admin(
            real_name,
            user_name,
            pass_word
        )
        new_admin.save()
    except IntegrityError:
        flash("error", "credentials anda duplicated")
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "berhasil menambahkan admin")

    return redirect(url_for("dashboard.admin"))


@dashboard_account_bp.route("/admin/edit/<id>", methods=["POST"])
@login_required
@admin_required
def admin_edit(id: str):
    """
    represents admin account edit processing url
    """

    admin = Admin.query.get(id)
    real_name = request.form.get("real_name")
    user_name = request.form.get("user_name")
    pass_word = request.form.get("pass_word")

    if admin is None:
        flash("error", "user admin tidak ditemukan")
        return redirect(url_for("dashboard.admin"))

    try:
        admin.set_real_name(real_name)
        admin.set_user_name(user_name)
        admin.set_pass_word(pass_word)
        admin.save()
    except IntegrityError:
        flash("error", "credentials anda duplicated")
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "berhasil update admin")

    return redirect(url_for("dashboard.admin"))


@dashboard_account_bp.route("/admin/delete/<id>")
@login_required
@admin_required
def admin_delete(id: str):
    """
    represents admin account delete processing url
    """

    admin = Admin.query.get(id)

    if admin is None:
        flash("error", "user admin tidak ditemukan")
    else:
        admin.delete()
        flash("success", "berhasil delete user admin")

    return redirect(url_for("dashboard.admin"))


@dashboard_account_bp.route("/member/delete/<id>")
@login_required
@admin_required
def member_delete(id: str):
    """
    represents member account delete processing page
    """

    member = Member.query.get(id)

    if member is None:
        flash("error", "member tidak ditemukan")
    else:
        member.delete()
        flash("success", "berhasil delete member")

    return redirect(url_for("dashboard.member"))
