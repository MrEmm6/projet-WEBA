from .forms import FilmForm
from .models import Film
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# Create your views here.

def list_films_seen(request):
    list_films = Film.objects.order_by('-dateVue')
    return render(request, 'films/list_films_seen.html', {'list_films' : list_films})

def ajout_film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list_films_seen')
    else:
        form = FilmForm()
    return render(request, 'films/ajout_film.html', {'form': form})

def modif_film(request, pk):
    post = get_object_or_404(Film, pk=pk)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list_films_seen')
    else:
        form = FilmForm(instance=post)
    return render(request, 'films/modif_film.html', {'form': form})