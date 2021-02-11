# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/dashboard/order.py
# Last Modified  : 02/11/21, 23:46 PM
# Copyright © Relarizky 2021


import pdfkit
from os import getcwd
from app.model import Order
from flask_login import login_required
from help.app.auth import admin_required
from help.app.email import EmailConfirmation
from help.app.blueprint import NestedBlueprint
from controller.dashboard.dashboard import dashboard_bp
from flask import (
    render_template, flash, url_for,
    redirect, request, send_from_directory
)


dashboard_order_bp = NestedBlueprint(
    dashboard_bp,
    "/order"
)


@dashboard_order_bp.route("/paid")
@login_required
@admin_required
def order_paid():
    """
    represents paid off order list page
    """

    order_list = Order.query.filter_by(paid_off=True).all()

    return render_template(
        "dashboard/order/paidoff.html",
        order_list=order_list
    )


@dashboard_order_bp.route("/paid/table")
def order_paid_table():
    """
    represents paid off order list in table
    """

    order_list = Order.query.filter_by(paid_off=True).all()

    return render_template(
        "dashboard/order/pdfable.html",
        order_list=order_list
    )


@dashboard_order_bp.route("/paid/pdf")
@login_required
@admin_required
def order_paid_pdf():
    """
    represents paid off order list generate pdf processing url
    """

    try:
        DIR = getcwd() + "/asset/"
        FILE = "paidoff.pdf"
        pdfkit.from_url(
            url_for(
                "dashboard.order_paid_table",
                _external=True
            ),
            DIR + FILE
        )
    except Exception as Error:
        flash("error", "terjadi kesalahan saat membuat file pdf")
        return redirect(url_for("dashboard.order_paid"))
    else:
        return send_from_directory(DIR, FILE, as_attachment=True)


@dashboard_order_bp.route("/unpaid")
@login_required
@admin_required
def order_unpaid():
    """
    represents unpaid off order list page
    """

    order_list = Order.query.filter_by(paid_off=False).all()

    return render_template(
        "dashboard/order/unpaidoff.html",
        order_list=order_list
    )


@dashboard_order_bp.route("/edit/<id>", methods=["POST"])
@login_required
@admin_required
def order_edit(id: str):
    """
    represents order status edit processing page
    """

    order = Order.query.get(id)

    if order is None:
        flash("error", "pemesanan tidak ditemukan")
        return redirect(url_for("dashboard.order_unpaid"))

    status = request.form.get("status")

    try:
        if bool(status) is True:
            print("ngnetot")
            email = EmailConfirmation.order_confirmation(
                order.member.email,
                order.product.name
            )
            email.send_mail()
        order.set_paid_off(status)
        order.save()
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "berhasil update status pemesanan")

    return redirect(request.headers.get("referer"))


@dashboard_order_bp.route("/delete/<id>")
@login_required
@admin_required
def order_delete(id: str):
    """
    represents order delete processing page
    """

    order = Order.query.get(id)

    if order is None:
        flash("error", "pemesanan tidak ditemukan")
    else:
        order.delete()
        flash("success", "berhasil menghapus pemesanan")

    return redirect(request.headers.get("referer"))
