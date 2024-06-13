from django.core.management.base import BaseCommand
from ...models import Author
from faker import Faker

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = 'Create author.'

    def handle(self, *args, **options):
        for i in range(10):
            author = Author(
                first_name=fake.first_name_male(),
                last_name=fake.last_name(),
                email=fake.email(),
                bio=fake.catch_phrase(),
                birthday=fake.date()
            )
            author.save()
            self.stdout.write(f'{author.full_name()} created!')
        self.stdout.write(f'Authors added to database')
