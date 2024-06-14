from django.core.management.base import BaseCommand
from ...models import Customer


class Command(BaseCommand):
    help = "Update Customer."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument("name", type=str, help="Customer name", default=None)
        parser.add_argument("email", type=str, help="Customer email", default=None)
        parser.add_argument("phone", type=str, help="Customer phone number", default=None)

    def handle(self, *args, **options):
        pk = options.get("pk")
        name = options.get("name")
        email = options.get("email")
        phone = options.get("phone")
        customer = Customer.objects.filter(pk=pk).first()
        if name is not None:
            customer.name = name
        if email is not None:
            customer.email = email
        if phone is not None:
            customer.phone = phone
        customer.save()
        self.stdout.write(self.style.SUCCESS(f"Customer {pk} updated."))
