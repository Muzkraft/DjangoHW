from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random
from .models import CoinFlip, Author, Post, Comment
from logging import Logger
from .forms import RandomForm, AuthorForm, PostForm

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


def pick_game(request):
    if request.method == 'POST':
        form = RandomForm(request.POST)
        if form.is_valid():
            event_type = form.cleaned_data['event_type']
            attempts = form.cleaned_data['attempts']
            if event_type == 'coin':
                return coin_flips(request, attempts)
            elif event_type == 'dice':
                return dice(request, attempts)
            elif event_type == 'numbers':
                return random_number(request, attempts)
    else:
        form = RandomForm()
    context = {'title': 'Pick a game', 'form': form}
    return render(request, 'sem1app1/pick_game.html', context)


def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = Author.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                bio=data['bio'],
                birthday=data['birthday'],
            )
            logger.info('Author saved to database')
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {'title': 'Add Author', 'form': form, 'authors': authors}
    return render(request, 'sem1app1/add_author.html', context)


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            post = Post.objects.create(
                title=data['title'],
                content=data['content'],
                author=['author'],
                category=['category'],
                is_published=data['is_published'],
            )
            logger.info('Post saved to database')
            # return redirect(f'{Author.first_name} posts')
    else:
        form = PostForm()
    posts = Post.objects.all()
    context = {'title': 'Add Post', 'form': form, 'posts': posts}
    return render(request, 'sem1app1/add_post.html', context)
