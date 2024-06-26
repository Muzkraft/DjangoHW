from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dice/<int:tries>/', views.dice, name='throw dice'),
    path('random-number/<int:tries>/', views.random_number, name='random number'),
    path('coin-flips/<int:tries>/', views.coin_flips, name='coin flips'),
    path('posts/<int:author_id>/', views.view_posts, name=f'{views.Author.first_name} posts'),
    path('full-post/<int:post_id>', views.full_post, name=f'full post'),
    path('pick-game/', views.pick_game, name=f'pick_game'),
    path('add-author/', views.author_form, name=f'create_author'),
    path('add-post/', views.post_form, name=f'create_post'),
]