from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from import_export.admin import ImportExportActionModelAdmin

from .forms import CustomerForm, ProductForm, OrderForm
from .models import Customer, Product, Order
from .admin_mixins import ExportAsCSVMixin


class SoldOutFilter(SimpleListFilter):
    title = "Sold out"
    parameter_name = "sold_out"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(quantity=0)
        else:
            return queryset.exclude(quantity=0)


class OrderInline(admin.TabularInline):
    model = Order

    readonly_fields = ['total_price', 'order_date', 'order_status']
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = True


@admin.action(description='Изменить статус заказа на "Выполнен"')
def change_order_status_true(modeladmin, request, queryset):
    queryset.update(order_status=True)


@admin.action(description='Изменить статус заказа на "В процессе"')
def change_order_status_false(modeladmin, request, queryset):
    queryset.update(order_status=False)


@admin.register(Customer)
class CustomerAdmin(ImportExportActionModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    ordering = ['registration_date']
    list_filter = ['name']
    search_fields = ['name', 'phone']
    search_help_text = 'Поиск по телефону(phone)'

    readonly_fields = ['registration_date']
    inlines = [OrderInline]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Адрес клиента',
                'fields': ['address', 'registration_date'],
            },
        ),
        (
            'Контакты',
            {
                'classes': ['collapse'],
                'description': 'Контакты клиента',
                'fields': ['phone', 'email'],
            },
        ),
    ]


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = (
        'title',
        'description',
        'quantity',
        'added_to_cart_date',
        'product_image',
        'display_sold_out',
        'display_price'
    )

    ordering = ['added_to_cart_date', 'price']
    list_filter = ['title', 'added_to_cart_date', 'quantity', SoldOutFilter]
    search_fields = ['title', 'added_to_cart_date', 'quantity', 'description']
    search_help_text = 'Поиск по названию, описанию, количеству, по дате добавления в корзину'

    readonly_fields = ['added_to_cart_date']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title', 'price', 'quantity'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Описание товара',
                'fields': ['description', 'product_image'],
            },
        ),
    ]

    def display_sold_out(self, obj):
        return obj.quantity == 0

    display_sold_out.short_description = "Sold out"
    display_sold_out.boolean = True

    def display_price(self, obj):
        return f"{obj.price} р."

    display_price.short_description = "Price"
    display_price.admin_order_field = "price"


@admin.register(Order)
class OrderAdmin(ImportExportActionModelAdmin):
    list_display = ['buyer', 'total_price', 'order_date', 'order_status']
    readonly_fields = ['buyer', 'total_price', 'order_date', 'order_status']
    actions = [change_order_status_true, change_order_status_false]
    form = OrderForm
