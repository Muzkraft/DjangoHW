from django import forms
from django.forms import ModelForm

from .models import Customer, Product


# форма создания новго клиента
class CustomerForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "mail@example.com"}
        ),
    )
    phone = forms.CharField(
        max_length=11,
        label="Phone number",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+7(999)999-99-99 "}
        ),
    )
    address = forms.CharField(
        max_length=100,
        label="Address",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your address"}
        ),
    )


class ProductForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Product name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter product name"}
        ),
    )
    description = forms.CharField(
        label="Product description",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter product description"}
        ),
    )
    price = forms.DecimalField(
        label="Product price",
        max_digits=100,
        decimal_places=2,
        initial=0,
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter product price"}
        ),
    )
    quantity = forms.IntegerField(
        label="Product quantity",
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    product_image = forms.ImageField(
        label="Product image",
        widget=forms.FileInput(attrs={"class": "form-control", "type": "file"}),
    )


class OrderForm(ModelForm):
    buyer = forms.ModelChoiceField(queryset=Customer.objects.all())
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple
    )
