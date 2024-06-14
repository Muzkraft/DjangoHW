from django.core.management.base import BaseCommand
from ...models import Customer


class Command(BaseCommand):
    help = 'Get all Customers.'

    def handle(self, *args, **options):
        customers = Customer.objects.all()
        self.stdout.write(f'{customers}')
