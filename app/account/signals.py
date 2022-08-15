import os

from django.core.mail import send_mail
from django.db.models.signals import post_save

from .models import Message


def message_notification(sender, instance, created, **kwargs):
    if created:
        message_form_data = instance
        subject = f'New message from: {message_form_data.sender_name}' \
                  f'{" from " + message_form_data.company if message_form_data.company else ""}.'

        message = f'Contact: {message_form_data.sender_email}\n' \
                  f'\n' \
                  f'{message_form_data.message}'

        if int(os.environ.get('TOGGLE_SES')):
            send_mail(
                subject=subject,
                message=message,
                from_email=os.environ.get('AWS_SES_EMAIL'),
                recipient_list=[os.environ.get('ACCOUNT_OWNER')],
                fail_silently=False
            )


post_save.connect(receiver=message_notification, sender=Message)
