import uuid

import ollama
from django.template.defaultfilters import title

from .forms import FilmForm
from .models import Film
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import AIItem
from .forms import AiForm
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

def ai_test(request):
    ai_items = AIItem.objects.all()
    return render(request, "films/aiTest.html", {"ai_items" : ai_items})

def add_ai(request):
    if request.method == "GET":
        form = AiForm()
        return render(request, "films/add_ai.html", {"form" : form})
    elif request.method == "POST":
        form = AiForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data["title"]
            ai_prompt = form.cleaned_data["description"]
            reponse = ollama.chat(
                model="gpt-oss:20b-cloud",
                messages=[{"role" : "user", "content" : ai_prompt}]
            )
            content = reponse["message"]["content"]
            AIItem.objects.create(
                title=titre,
                description=ai_prompt,
                steps=content,
            )
            return redirect("aiTest")
    return  redirect("aiTest")

def prompt_delete(request, pk):
    post = get_object_or_404(AIItem, pk=pk)
    post.delete()
    return redirect("aiTest")
