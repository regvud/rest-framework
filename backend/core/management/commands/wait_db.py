import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')

        db_con = False

        while not db_con:
            try:
                connection.ensure_connection()
                db_con = True
            except OperationalError:
                self.stdout.write('Database is unavailable, wait 3 sec... ')
                time.sleep(3)

        self.stdout.write('Connection to database is successful!')
