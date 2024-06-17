from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("orders/<int:customer_id>", views.orders, name="orders"),
    path("orders/", views.orders, name="show_all_orders"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("add_product/", views.add_product, name="add_product"),
    path("add_order/", views.add_order, name="add_order"),
]