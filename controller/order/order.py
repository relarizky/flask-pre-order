# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/order/order.py
# Last Modified  : 02/09/21, 22:37 PM
# Copyright © Relarizky 2021


from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import current_user, login_required
from help.token import create_token, confirm_token
from help.app.auth import verified_required, member_required, token_required
from help.app.email import EmailConfirmation
from app.model import Order, Product


order_bp = Blueprint(
    "order",
    __name__,
    template_folder="view/"
)


@order_bp.route("/paid")
@login_required
@member_required
@verified_required
def order_paid():
    """
    represents member paid order list page
    """

    order_list = Order.query.filter_by(
        paid_off=True,
        id_member=current_user.id
    ).all()

    return render_template("order/paidoff.html", order_list=order_list)


@order_bp.route("/unpaid")
@login_required
@member_required
@verified_required
def order_unpaid():
    """
    represents member unpaid order list page
    """

    order_list = Order.query.filter_by(
        paid_off=False,
        id_member=current_user.id
    ).all()

    return render_template("order/unpaidoff.html", order_list=order_list)


@order_bp.route("/process/<id>", methods=["POST"])
@login_required
@member_required
@verified_required
def order_process(id: str):
    """
    represents order processing url
    """

    pieces = request.form.get("pieces")
    address = request.form.get("address")

    try:
        order = Order(pieces, address)
        order.set_object_member(current_user.id)
        order.set_object_product(id)
        order.save()
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash(
            "success",
            "sukses order barang, silahkan edit info pembayaran"
        )

    return redirect(url_for("order.order_unpaid"))


@order_bp.route("/edit/<id>", methods=["POST"])
@login_required
@member_required
@verified_required
def order_edit(id: str):
    """
    represents edit order processing url
    """

    order = Order.query.get(id)

    if order is None:
        flash("error", "produk tidak ditemukan")
        return redirect(url_for("index.index"))

    proof = request.files.get("proof")
    pieces = request.form.get("pieces")
    address = request.form.get("address")

    try:
        order.set_pieces(pieces)
        order.set_address(address)
        order.set_payment_proof(proof)
        order.save()
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "sukses mengubah info pemesanan")

    return redirect(url_for("order.order_unpaid"))

@order_bp.route("/delete/<id>")
@login_required
@member_required
@verified_required
def order_delete(id: str):
    """
    represents delete order processing url
    """

    order = Order.query.get(id)

    if order is None:
        flash("error", "pemesanan tidak ditemukan")
    else:
        order.delete()
        flash("success", "sukses delete pemesanan")

    return redirect(url_for("order.order_unpaid"))
