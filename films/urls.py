from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_films_seen, name='list_films_seen'),
    path('film/<int:pk>/modif/', views.modif_film, name='modif_film'),
    path('film/ajout/', views.ajout_film, name='ajout_film'),
]