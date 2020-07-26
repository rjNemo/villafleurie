from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import mail_admins, send_mail

from villafleurie.settings import EMAIL_HOST_USER


""" Mailer Service used to send messages using Gmail.
    All Mailers must implement the following methods:

    def send_confirmation(name, email)->void

    def send_notification(name, email, subject, message)->void

    def send_quotation(name, email)->void
    """


@shared_task
def send_confirmation(name, email):
    """ Send confirmation message to customer """
    subject = "Nous avons reçu votre message"
    message = f" Merci {name}, Bien reçu nous revenons vers vous rapidement !"

    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email]  
    )


@shared_task
def send_notification(name, email, subject, message):
    """ Send notification to admins """

    mail_admins(
        f"{name} a envoyé un message",
        f"Sujet : {subject}\nDe : {name}, {email}\nMessage : {message}"
    )


@shared_task
def send_quotation(name, email):
    """ Send quotation to customer """
    send_confirmation_mail(name, email)  
