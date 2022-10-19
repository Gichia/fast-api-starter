"""
Contains utility function to send emails via MailGun SMTP servers.

Classes:
--------
    None

Functions:
----------
    send_email():
        a utility function to send emails vias MailGun

Misc Variables:
--------------
    settings: the settings config to get env variabled
"""

from requests import Response, post

from app.config import Settings


settings = Settings()


class Mailgun:
    """
    The Mailgun class
    ..........
    """
    @classmethod
    async def send_email(
            cls, emails: list[str], subject: str, html: str) -> Response:
        """
        Send emails to the defined recipients using MailGun servers

        Parameters:
        ----------
            emails: list[str]
                the list of recipient emails
            subject: str
                the subject of the email
            html: str
                the html template

        Returns:
        -------
            Response:
                The Response object, which contains a server's
                response to an HTTP request.
        """
        return post(
            f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages",
            auth=("api", f"{settings.MAILGUN_API_KEY}"),
            data={
                "from": f"{settings.FROM_TITLE} <{settings.FROM_EMAIL}>",
                "to": emails,
                "subject": subject,
                "html": html,
            })
