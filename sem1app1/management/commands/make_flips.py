import random

from django.core.management.base import BaseCommand
from ...models import CoinFlip


class Command(BaseCommand):
    help = 'Generate fake flips.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='flips')

    def handle(self, *args, **options):
        count = options.get('count')
        for i in range(1, count + 1):
            flip = CoinFlip(result=f'{random.choice(['head', 'tail'])}')
            flip.save()
