from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'List all database tables'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            if tables:
                self.stdout.write("Database tables:")
                for table in tables:
                    self.stdout.write(f"- {table[0]}")
            else:
                self.stdout.write("No tables found in database")
