from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = 'Get user by id.'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User id')

    def handle(self, *args, **options):
        id = options['id']
        user = User.objects.get(id=id)
        self.stdout.write(f'{user}')
