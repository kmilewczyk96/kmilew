from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save

from .models import Account, Message


def message_notification(sender, instance, created, **kwargs):
    if created:
        message_form_data = instance
        subject = f'New message from: {message_form_data.sender_name}' \
                  f'{" from " + message_form_data.company if message_form_data.company else ""}.'

        message = f'Contact: {message_form_data.sender_email}\n' \
                  f'\n' \
                  f'{message_form_data.message}'

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[Account.objects.first().owner.email],
            fail_silently=False
        )


post_save.connect(receiver=message_notification, sender=Message)
