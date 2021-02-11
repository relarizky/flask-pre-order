# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/dashboard/product.py
# Last Modified  : 02/05/21, 16:37 PM
# Copyright © Relarizky 2021


from flask import render_template, url_for, redirect, flash, request
from flask_login import login_required
from help.app.auth import admin_required
from help.app.blueprint import NestedBlueprint
from controller.dashboard.dashboard import dashboard_bp
from app.model import Product, Category


dashboard_product_bp = NestedBlueprint(
    dashboard_bp,
    "/product"
)


@dashboard_product_bp.route("/")
@login_required
@admin_required
def product():
    """
    represents product list page
    """

    categories = Category.query.all()
    product_list = Product.query.all()

    return render_template(
        "dashboard/product/product.html",
        categories=categories,
        product_list=product_list
    )


@dashboard_product_bp.route("/add", methods=["POST"])
@login_required
@admin_required
def product_add():
    """
    represents add product processing url
    """

    name = request.form.get("name")
    price = request.form.get("price")
    picture = request.files.get("picture")
    category = request.form.get("category")

    try:
        new_product = Product(name, price, picture)
        new_product.set_object_category(category)
        new_product.save()
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "sukses tambah produk")

    return redirect(url_for("dashboard.product"))


@dashboard_product_bp.route("/edit/<id>", methods=["POST"])
@login_required
@admin_required
def product_edit(id: str):
    """
    represents edit product processing url
    """

    product = Product.query.get(id)

    if product is None:
        flash("error", "produk tidak ditemukan")
        return redirect(url_for("dashboard.product"))

    name = request.form.get("name")
    price = request.form.get("price")
    status = request.form.get("status")
    picture = request.files.get("picture")
    category = request.form.get("category")

    try:
        product.set_name(name)
        product.set_price(price)
        product.set_status(status)
        product.set_picture(picture)
        product.set_object_category(category)
        product.save()
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "sukses update produk")

    return redirect(url_for("dashboard.product"))


@dashboard_product_bp.route("/delete/<id>")
@login_required
@admin_required
def product_delete(id: str):
    """
    represents delete product processing url
    """

    product = Product.query.get(id)

    if product is None:
        flash("error",  "produk tidak ditemukan")
    else:
        product.delete()
        flash("success", "sukses menghapus produk")

    return redirect(url_for("dashboard.product"))
