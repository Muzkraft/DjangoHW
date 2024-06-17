from decimal import Decimal
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"Name: {self.name},"
                f" email: {self.email},"
                f" phone {self.phone},"
                f" address: {self.address},"
                f" registered: {self.registration_date}"
                )


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    added_to_cart_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title}, price: {self.price}, quantity: {self.quantity}"


class Order(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client: {self.buyer}, total amount = {self.total_amount}"

    def calculate_total(self):
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        self.total_price = total
        self.save()
