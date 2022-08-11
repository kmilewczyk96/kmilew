"""
Force Django to wait for database until it's available.
"""
import os

from django.db.models import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from core.models import User


class Command(BaseCommand):
    """Django custom command to create superuser if he does not exist."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        user_model = User
        try:
            user_model.objects.get(email=os.environ.get('ACCOUNT_OWNER'))
        except ObjectDoesNotExist:
            user_model.objects.create_superuser(
                email=os.environ.get('ACCOUNT_OWNER'),
                password=os.environ.get('ACCOUNT_PASS')
            )
            self.stdout.write(self.style.SUCCESS('SUPERUSER CREATED!'))
        else:
            self.stdout.write(self.style.SUCCESS('SUPERUSER ALREADY EXISTS!'))
