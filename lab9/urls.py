from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('/start', views.renders),
    path('/input',views.index),
    path('/books_for_genre', views.books_for_genre),
    path('/author_for_genres', views.author_for_genres),
    path('/sort_date', views.dates),
]
