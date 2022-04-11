from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from django_celery.settings import EMAIL_HOST_USER


# Send NewsLetter
@shared_task
def send_message(email, subject, message):
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )