from django.core.management.base import BaseCommand
from home2_app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='qwerty', email='qwerty@example.com', phone='1352661760', address='qwerty 123')
        client.save()
        self.stdout.write(f'{client}')