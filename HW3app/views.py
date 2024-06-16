import logging
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datetime import timedelta
from .models import Order, Customer, Product

logger = logging.getLogger(__name__)


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
            "client": customer,
            "order": order,
            "products_week": products_week,
            "products_month": products_month,
            "products_year": products_year,
        }
    else:
        order = Order.objects.all()
        context = {"title": f"Orders list", "order": order}
    return render(request, "HW3app/orders.html", context)
