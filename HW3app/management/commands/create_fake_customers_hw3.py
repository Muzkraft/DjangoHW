from django.core.management.base import BaseCommand
from ...models import Customer
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Create fake Customers."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='customers count')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            customer = Customer(
                name=fake.first_name_male(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            customer.save()
            self.stdout.write(self.style.SUCCESS(f"{customer} added to database."))
        self.stdout.write(self.style.SUCCESS('All customers added'))
