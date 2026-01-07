from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_films_seen, name='list_films_seen'),
    path('film/<int:pk>/modif/', views.modif_film, name='modif_film'),
    path('film/ajout/', views.ajout_film, name='ajout_film'),
    path('film/ai', views.ai_test, name='aiTest'),
    path("film/ai/add", views.add_ai, name="add_ai"),
    path('film/ai/<int:pk>/', views.prompt_delete, name='prompt_delete'),
]