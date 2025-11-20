from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_films_seen, name='list_films_seen'),
]