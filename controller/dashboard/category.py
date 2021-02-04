# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/dashboard/category.py
# Last Modified  : 02/04/21, 22:08 PM
# Copyright © Relarizky 2021


from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required
from help.app.auth import admin_required
from help.app.blueprint import NestedBlueprint
from controller.dashboard.dashboard import dashboard_bp
from sqlalchemy.exc import IntegrityError
from app.model import Category


dashboard_category_bp = NestedBlueprint(
    dashboard_bp,
    "/category"
)


@dashboard_category_bp.route("/")
@login_required
@admin_required
def category():
    """
    represents category list page
    """

    categories = Category.query.all()

    return render_template(
        "dashboard/category/category.html",
        categories=categories
    )


@dashboard_category_bp.route("/add", methods=["POST"])
@login_required
@admin_required
def category_add():
    """
    represents add category processing url
    """

    name = request.form.get("name")

    try:
        category = Category(name)
        category.save()
    except IntegrityError:
        flash("error", "kategori yang anda masukan duplicated")
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "sukses menambah kategori")

    return redirect(url_for("dashboard.category"))


@dashboard_category_bp.route("/edit/<id>", methods=["POST"])
@login_required
@admin_required
def category_edit(id: str):
    """
    represents edit category processing url
    """

    category = Category.query.get(id)

    if category is None:
        flash("error", "kategori tidak ditemukan")
        return redirect(url_for("dashboard.category"))

    name = request.form.get("name")

    try:
        category.set_name(name)
        category.save()
    except IntegrityError:
        flash("error", "kategori yang anda masukan duplicated")
    except Exception as Error:
        flash("error", Error.__str__())
    else:
        flash("success", "sukses update kategori")

    return redirect(url_for("dashboard.category"))


@dashboard_category_bp.route("/delete/<id>")
@login_required
@admin_required
def category_delete(id: str):
    """
    represents delete category processing url
    """

    category = Category.query.get(id)

    if category is None:
        flash("error", "kategori tidak ditemukan")
    else:
        category.delete()
        flash("success", "berhasil menghapus kategori")

    return redirect(url_for("dashboard.category"))
