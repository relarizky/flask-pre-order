# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/model.py
# Last Modified  : 01/26/21, 11:30 PM
# Copyright © Relarizky 2021


from app import sql as db
from datetime import datetime
from flask_login import UserMixin
from help.database import DBHelper, create_uuid
from help.exception import ObjectDoesNotExist

from help.setter.order_setter import OrderSetter
from help.setter.admin_setter import AdminSetter
from help.setter.member_setter import MemberSetter
from help.setter.product_setter import ProductSetter
from help.setter.category_setter import CategorySetter


class Admin(db.Model, UserMixin, DBHelper, AdminSetter):
    """
    represents tb_admin
    """

    __tablename__ = "tb_admin"

    id = db.Column(db.String(5), primary_key=True)
    real_name = db.Column(db.String(40), nullable=False, unique=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    pass_word = db.Column(db.String(56), nullable=False)

    def __init__(self, realname: str, username: str, password: str) -> None:
        self.id = create_uuid()
        self.set_real_name(realname)
        self.set_user_name(username)
        self.set_pass_word(password)


class Member(db.Model, UserMixin, DBHelper, MemberSetter):
    """
    represents tb_member
    """

    __tablename__ = "tb_member"

    id = db.Column(db.String(5), primary_key=True)
    real_name = db.Column(db.String(40), nullable=False, unique=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    pass_word = db.Column(db.String(56), nullable=False)
    phone = db.Column(db.String(12), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)

    def __init__(self, realname: str, username: str,
                 password: str, phone: str, email: str) -> None:
        self.id = create_uuid()
        self.set_real_name(realname)
        self.set_user_name(username)
        self.set_pass_word(password)
        self.set_phone_number(phone)
        self.set_email_address(email)


class Category(db.Model, DBHelper, CategorySetter):
    """
    represents tb_category
    """

    __tablename__ = "tb_category"

    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    product = db.relationship("Product", backref="category", lazy="dynamic")

    def __init__(self, name: str) -> None:
        self.id = create_uuid()
        self.set_name(name)


class Product(db.Model, DBHelper, ProductSetter):
    """
    represents tb_product
    """

    __tablename__ = "tb_product"

    id = db.Column(db.String(5), primary_key=True)
    id_category = db.Column(db.String(5), db.ForeignKey("tb_category.id"))
    name = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Integer, default=0)
    picture = db.Column(db.String(36), default="unknown.jpg")
    order = db.relationship("Order", backref="product", lazy="dynamic")

    def __init__(self, name: str, price: int, picture: str = None) -> None:
        self.id = create_uuid()
        self.set_name(name)
        self.set_price(price)
        self.set_picture(picture)

    def set_object_category(self, id_category: str) -> None:
        """
        set category by its id
        """

        category = Category.query.get(id_category)

        if category is None:
            raise ObjectDoesNotExist("kategori tidak ditemukan")

        self.category = category


class Order(db.Model, DBHelper, OrderSetter):
    """
    represents tb_order
    """

    __tablename__ = "tb_order"

    id = db.Column(db.String(5), primary_key=True)
    id_member = db.Column(db.String(5), db.ForeignKey("tb_member.id"))
    id_product = db.Column(db.String(5), db.ForeignKey("tb_product.id"))
    pieces = db.Column(db.SmallInteger, default=0)
    paid_off = db.Column(db.Boolean, default=False)
    payment_proof = db.Column(db.String(36), default="unknown.jpg")
    ordered_on = db.Column(db.Date, default=datetime.now())

    def __init__(self, pieces: int, paid_off: bool, payment_proof: str) -> None:
        self.id = create_uuid()
        self.set_pieces(pieces)
        self.set_paid_off(paid_off)
        self.set_payment_proof(payment_proof)

    def set_object_member(self, member_id: str) -> None:
        """
        set order member
        """

        member = Member.query.get(member_id)

        if member is None:
            raise ObjectDoesNotExist("member tidak dikenal")

        self.member = member

    def set_object_product(self, product_id: str) -> None:
        """
        set product by its id
        """

        product = Product.query.get(product_id)

        if product is None:
            raise ObjectDoesNotExist("produk tidak ditemukan")

        self.product = product
