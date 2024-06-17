import random
from django.core.management.base import BaseCommand
from ...models import Customer, Product, Order


class Command(BaseCommand):
    help = "Create orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='orders count')
    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            customer = Customer.objects.get(pk=i)
            prods = []
            prods = [Product.objects.get(pk=random.randint(1, 10)) for _ in range(3)]
            order = Order.objects.create(buyer=customer)
            order.products.add(*prods)
            order.calculate_total()
            order.save()
        self.stdout.write(self.style.SUCCESS("All orders added to database"))
