from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from .models import CoinFlip, Author, Post
from logging import Logger

logger = Logger(__name__)


def home(request):
    return HttpResponse(f'<h1>Welcome to random games!</h1>')


def oreshka(request):
    return HttpResponse(f"It is {random.choice(['Орёл', 'Решка'])}")


def dice(request, tries=1):
    logger.info('Dice page access')
    dices = [random.randint(1, 6) for _ in range(tries)]
    context = {'title': 'Random dice', 'content': dices}
    return render(request, 'sem1app1/games.html', context)


def random_number(request, tries=1):
    logger.info('Random number page access')
    num_list = [random.randint(1, 101) for _ in range(tries)]
    context = {'title': 'Random number', 'content': num_list}
    return render(request, 'sem1app1/games.html', context)


def coin_flips(request, tries=1):
    logger.info('Coin flip page access')

    flips_list = [random.choice(['орёл', 'решка']) for _ in range(tries)]

    context = {'title': 'flip coin', 'content': flips_list}
    # flips = CoinFlip.statistic(5)
    return render(request, 'sem1app1/games.html', context)


def view_posts(request, author_id):
    author = Author.objects.filter(pk=author_id).first()
    content = Post.objects.filter(author=author_id).all()
    context = {'title': f'{author.full_name()}', 'content': content}
    return render(request, 'sem1app1/posts.html', context)


def full_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.add_view()
    post.save()
    context = {'title': f'{post.author.full_name()}', 'post': post}
    return render(request, 'sem1app1/full-post.html', context)
