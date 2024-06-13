import random

from django.core.management.base import BaseCommand
from ...models import Post, Author
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = 'Create post.'

    def handle(self, *args, **options):
        author_ids = Author.objects.all()
        for author in author_ids:
            post = Post(
                title=fake.catch_phrase(),
                content=fake.text(),
                author=Author.objects.filter(pk=random.randint(1, len(author_ids))).first(),
                category=fake.catch_phrase(),
                date=fake.date(),
                views=random.randint(1, 1000),
                is_published=random.randint(0, 1)
            )
            post.save()
            self.stdout.write(f'{post} created!')
        self.stdout.write(f'All posts created!')
