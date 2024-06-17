import datetime
from django import forms
from .models import Author


class RandomForm(forms.Form):
    EVENT_CHOICES = [
        ('coin', 'монета'),
        ('dice', 'кости'),
        ('numbers', 'числа'),
    ]

    event_type = forms.ChoiceField(choices=EVENT_CHOICES, label='Pick a game')

    attempts = forms.IntegerField(min_value=1, max_value=10, label='Number of attempts')


class AuthorForm(forms.Form):
    first_name = forms.CharField(label='First name', required=True, max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Few words about author')
    birthday = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                          'type': 'date'}))


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Write a post here')
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100)
    is_published = forms.BooleanField(initial=False)
