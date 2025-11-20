from django.shortcuts import render
from .models import Film
# Create your views here.

def list_films_seen(request):
    list_films = Film.objects.order_by('-dateVue')
    return render(request, 'films/list_films_seen.html', {'list_films' : list_films})