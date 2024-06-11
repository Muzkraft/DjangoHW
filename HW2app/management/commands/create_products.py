import random

from django.core.management.base import BaseCommand
from ...models import Product
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='products count')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            product = Product(
                title=f"product{i}",
                description=fake.catch_phrase(),
                price=random.randint(1, 1000) * 1.33,
                quantity=random.randint(1, 100),
            )
            product.save()
        self.stdout.write(self.style.SUCCESS("Products added to database."))
