from django.core.management.base import BaseCommand
from ...models import Customer


class Command(BaseCommand):
    help = "Get customer."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        self.stdout.write(f'{customer}')
