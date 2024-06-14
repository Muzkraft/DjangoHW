from . import views
from django.urls import path

urlpatterns = [
    path('orders/<int:customer_id>', views.orders, name='orders'),
    path('orders/', views.orders, name='all_orders'),
]