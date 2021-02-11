# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : app/register.py
# Last Modified  :  02/11/21, 23:51 PM
# Copyright © Relarizky 2021


from app import apps, api
from api.category import CategoryAPI
from controller.auth.auth import auth_bp
from controller.index.index import index_bp
from controller.order.order import order_bp
from controller.dashboard.dashboard import dashboard_bp


# API
api.add_resource(CategoryAPI, "/category")

# route
apps.register_blueprint(index_bp, url_prefix="/")
apps.register_blueprint(auth_bp, url_prefix="/auth")
apps.register_blueprint(order_bp, url_prefix="/order")
apps.register_blueprint(dashboard_bp, url_prefix="/dashboard")
