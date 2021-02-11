# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : seeder.py
# Last Modified  :  02/12/21, 00:08 AM
# Copyright © Relarizky 2021


from app import apps
from app.model import Admin


admin_list = [
    [
        "administrator",
        "admin",
        "12345678"
    ],
    [
        "testadmin",
        "testadmin",
        "12345678"
    ]
]


def add_default_admin(credentials: list) -> None:
    """
    add default admin into database
    """

    with apps.app_context():
        admin = Admin(credentials[0], credentials[1], credentials[2])
        admin.save()


for admin in admin_list:
    add_default_admin(admin)


print("done.")
