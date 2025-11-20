from django.shortcuts import render

# Create your views here.

def list_films_seen(request):
    return render(request, 'films/list_films_seen.html', {})