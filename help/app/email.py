# Author    : Relarizky
# Github    : https://github.com/relarizky
# File Name : help/app/email.py
# Last Modified  : 01/30/21, 14:00 PM
# Copyright © Relarizky 2021


from app import apps, mail
from flask_mail import Message


class EmailConfirmation:
    """
    email confirmation sender
    """

    def __init__(self, receiver: str, subject: str, body: str) -> None:
        self.body = body
        self.subject = subject
        self.receiver = receiver

    @classmethod
    def register_confirmation(cls, receiver: str, url: str):
        """
        send register confirmation
        """

        email_subject = "register confirmation"
        email_message = f"""
        Konfirmasi registrasi anda\n
        Token akan expired dalam 10 menit\n\n\n
        {url}
        """.strip()

        return cls(receiver, email_subject, email_message)

    @classmethod
    def forgot_password_confirmation(cls, receiver: str, url: str):
        """
        send forgot password confirmation
        """

        email_subject = "forgot password confirmation"
        email_message = f"""
        Seseorang mencoba melakukan perubahan password\n
        Tolong konfirmasi bahwa ini anda\n\n\n
        {url}
        """.strip()

        return cls(receiver, email_subject, email_message)

    def send_mail(self):
        """
        send an email to receiver
        """

        message = Message(
            recipients=[self.receiver],
            subject=self.subject,
            body=self.body
        )

        with apps.app_context():
            mail.connect()
            mail.send(message)
