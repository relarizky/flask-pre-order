# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : controller/index/index.py
# Last Modified  : 02/07/21, 14:53 PM
# Copyright © Relarizky 2021


from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import current_user, login_required
from help.token import create_token
from help.app.auth import verified_required, member_required
from help.app.email import EmailConfirmation
from app.model import Product


index_bp = Blueprint(
    "index",
    __name__,
    template_folder="view/"
)


@index_bp.route("/")
@index_bp.route("/<int:page>")
@index_bp.route("/index/<int:page>")
@verified_required
def index(page: int = 1):
    """
    represents home page
    """

    products = Product.query.paginate(page, 6, True)

    return render_template("index/index.html", products=products)


@index_bp.route("/search")
@verified_required
def search():
    """
    represents search page
    """

    query = request.args.get("name")
    pages = request.args.get("page", 1, type=int)
    products = Product.query.filter(
        Product.name.like(f"%{query}%")
    ).paginate(pages, 6, True)

    return render_template(
        "index/search.html",
        query=query,
        products=products
    )


@index_bp.route("/category/<id>")
@verified_required
def category(id: str):
    """
    represents category page
    """

    pages = request.args.get("page", 1, type=int)
    products = Product.query.filter_by(
        id_category=id
    ).paginate(pages, 6, True)

    return render_template(
        "index/category.html",
        category=id,
        products=products
    )


@index_bp.route("/unverified")
@login_required
@member_required
def unverified():
    """
    represents unverified page
    """

    if current_user.verified:
        return redirect(url_for("index.index"))

    return render_template("index/unverified.html")


@index_bp.route("/resend")
@login_required
@member_required
def resend():
    """
    represents resend email url
    """

    email = EmailConfirmation.register_confirmation(
        current_user.email,
        url_for(
            "auth.register_confirmation_token",
            token=create_token(current_user.id, current_user.email),
            _external=True
        )
    )
    email.send_mail()

    flash("success", "berhasil mengirim ulang email, silahkan cek email anda")
    return redirect(url_for("index.index"))
