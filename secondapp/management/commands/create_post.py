from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **options):
        user = User(name='Sega', email='no1z555@gmail.com', password='secret', age=38)
        ...
        user.save()
        self.stdout.write(f'{user} created!')
