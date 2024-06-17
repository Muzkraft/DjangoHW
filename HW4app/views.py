import logging
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Order, Customer, Product
from .forms import CustomerForm, ProductForm, OrderForm
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'HW4app/index.html')


def orders(request, customer_id: int = None):
    if customer_id:
        logger.info(f'Accessed orders of customer {customer_id}')
        customer = get_object_or_404(Customer, pk=customer_id)
        order = Order.objects.filter(buyer=customer)
        today = timezone.now()

        weekly_orders = order.filter(order_date__gte=today - timedelta(days=7))
        monthly_orders = order.filter(order_date__gte=today - timedelta(days=30))
        yearly_orders = order.filter(order_date__gte=today - timedelta(days=365))

        products_week = {product for order in weekly_orders for product in order.products.all()}
        products_month = {product for order in monthly_orders for product in order.products.all()}
        products_year = {product for order in yearly_orders for product in order.products.all()}

        context = {
            "title": f"Customer orders {customer.name}",
            "customer": customer,
            "order": order,
            "products_week": products_week,
            "products_month": products_month,
            "products_year": products_year,
        }
    else:
        orders = Order.objects.all()
        context = {"title": f"Orders list", "orders": orders}
    return render(request, "HW4app/orders.html", context)


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Customer.objects.create(
                name=data["name"],
                email=data["email"],
                phone=data["phone"],
                address=data["address"],
            )
            logger.info(f"Customer added to database")
            return redirect('index')
    else:
        form = CustomerForm()
    context = {"title": "Customer registration", "form": form}
    return render(request, "HW4app/add_customer.html", context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            product = Product(
                title=data["title"],
                description=data["description"],
                price=data["price"],
                quantity=data["quantity"],
                product_image=data["product_image"],
            )
            fs = FileSystemStorage()
            fs.save(product.product_image.name, product.product_image)
            product.save()
            return redirect('index')
    else:
        form = ProductForm()
    products = Product.objects.all()
    context = {"title": "Add product", "form": form, "products": products}
    return render(request, "HW4app/add_product.html", context)


def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            buyer = form.cleaned_data["buyer"]
            prods = form.cleaned_data["products"]
            # quantity = form.cleaned_data["quantity"]
            order = Order.objects.create(buyer=buyer)
            order.products.add(*prods)
            order.calculate_total()
            order.save()
            return redirect('index')
    else:
        form = OrderForm()
    context = {"title": "Make an order", "form": form}
    return render(request, "HW4app/add_order.html", context)
