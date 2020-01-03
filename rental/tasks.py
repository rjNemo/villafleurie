from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail, mail_admins
from villafleurie.settings import EMAIL_HOST_USER, BASE_DIR
from rental.bookings import build_calendar_api_service
import os


@shared_task
def send_confirmation_mail(name, email, template="ticket"):
    """ Send confirmation message to customer """
    subject = "Nous avons reçu votre message"
    message = f" Merci {name}, Bien reçu nous revenons vers vous rapidement ! - HtmlMessage"

    html_path = os.path.join(BASE_DIR, 'rental/templates/rental/html/')
    with open(os.path.join(html_path, f"{template}.html"), 'r') as html:
        html_message = html.read()

    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email],
        html_message=html_message
    )


@shared_task
def send_notification(subject, name, message, template="activation"):
    """ Send notification to admins """
    html_path = os.path.join(BASE_DIR, 'rental/templates/rental/html/')
    with open(os.path.join(html_path, f"{template}.html"), 'r') as html:
        html_message = html.read()
    mail_admins(
        f"{name} a envoyé un message",
        f"Sujet : {subject}\nMessage : {message}",
        html_message=html_message
    )


@shared_task
def send_quotation(name, email):
    """ Send quotation to customer """
    send_confirmation_mail(name, email, template="welcome")
