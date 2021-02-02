# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/dashboard/dashboard.py
# Last Modified  : 02/02/21, 01:13 PM
# Copyright © Relarizky 2021


from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from app.model import Member, Product, Order
from help.app.auth import admin_required
from sqlalchemy.exc import IntegrityError


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    template_folder="view/"
)


@dashboard_bp.route("/")
@dashboard_bp.route("/index")
@login_required
@admin_required
def index():
    """
    represents dashboard home page
    """

    member = Member.query.count()
    product = Product.query.count()
    paid_off = Order.query.filter_by(paid_off=True).count()
    unpaid_off = Order.query.filter_by(paid_off=False).count()

    return render_template(
        "dashboard/index.html",
        total_member=member,
        total_product=product,
        total_paid_off=paid_off,
        total_unpaid_off=unpaid_off
    )


@dashboard_bp.route("/setting")
@login_required
@admin_required
def setting():
    """
    represents admin user setting page
    """

    return render_template("dashboard/setting.html")


@dashboard_bp.route("/setting/process", methods=["POST"])
@login_required
@admin_required
def setting_process():
    """
    represents admin user setting processing url
    """

    real_name = request.form.get("real_name")
    user_name = request.form.get("user_name")
    pass_word = request.form.get("pass_word")

    try:
        current_user.set_real_name(real_name)
        current_user.set_user_name(user_name)
        current_user.set_pass_word(pass_word)
        current_user.save()
    except IntegrityError:
        flash("error", "credentials anda duplicated")
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "sukses update profile ")

    return redirect(url_for("dashboard.setting"))
