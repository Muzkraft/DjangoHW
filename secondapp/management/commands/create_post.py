import random

from django.core.management.base import BaseCommand
from ...models import Post, Author
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = 'Create post.'

    def handle(self, *args, **options):
        post = Post(
            title=fake.catch_phrase(),
            content=fake.text(),
            author=Author.objects.filter(pk=1).first(),
            category=fake.catch_phrase()
        )
        post.save()
        self.stdout.write(f'{post} created!')
