"""
Force Django to wait for database until it's available.
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django custom command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        db_ready = False
        while db_ready is False:
            try:
                self.check(databases=['default'])
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Waiting for db to be available...')
                time.sleep(1)
            else:
                db_ready = True

        self.stdout.write(self.style.SUCCESS('DB is now available!'))
