from django.core.management.base import BaseCommand
from ...models import Customer
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Create fake Customer."

    def handle(self, *args, **kwargs):
        customer = Customer(
            name=fake.first_name_male(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        customer.save()
        self.stdout.write(self.style.SUCCESS(f"{customer} added to database."))
