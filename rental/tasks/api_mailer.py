""" Mailer Service used to send messages using API WebHooks.
    All Mailers must implement the following methods:

    def send_confirmation(name, email)->void

    def send_notification(name, email, subject, message)->void

    def send_quotation(name, email)->void
"""

from __future__ import absolute_import, unicode_literals

import os
from datetime import datetime

import requests
from celery import shared_task

from villafleurie.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST_USER

# get mailing hook URL from env
URL = os.environ.get("MAIL_HOOK")


@shared_task
def send_confirmation(name, email):
    """ Send confirmation message to customer """

    payload = {
        "mail_to": email,
        "from_name": DEFAULT_FROM_EMAIL,
        "reply_to": EMAIL_HOST_USER,
        "subject": f"[VillaFleurie] - {name}, nous avons reçu votre message",
        "body": f"Merci {name}, nous avons bien reçu votre message, nous revenons vers vous rapidement !\nCordialement,\nNilka (VillaFleurie)"
    }

    requests.post(URL, data=payload)


@shared_task
def send_notification(name, email, subject, message, date):
    """ Send notification to admins """

    payload = {
        "mail_to": EMAIL_HOST_USER,
        "from_name": DEFAULT_FROM_EMAIL,
        "reply_to": EMAIL_HOST_USER,
        "subject": f"{name} a envoyé un message",
        "body": f"Sujet : {subject}\nDe : {name}, {email}\nLe : {date}\nMessage : {message}\nCordialement,\nNilka (VillaFleurie)"
    }

    requests.post(URL, data=payload)


@shared_task
def send_quotation(name, email):
    """ Notify admins then send quotation to customer """

    send_notification(
        name,
        email,
        "Nouvelle demande de réservation",
        "Depuis le site",
        datetime.now()
    )

    send_confirmation(name, email)
