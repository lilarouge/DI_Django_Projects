from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

# Create your views here.

def index(request):
    return render(request, 'homepage.html')

def navbar(request):
    return render(request, 'navbar.html')

def add_film(request):
    if request.method == "GET":
        form = AddFilmForm()
        return render(request, "films/addFilms.html", {"form": form})
    if request.method == "POST":
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form= AddFilmForm()
    return render(request, "films/addFilms.html", {"form": form})

# Pas de relation pour les directeurs

def add_director(CreateView):
    model= Director
    form_class= AddDirectorForm
    template_name= 'director/addDirector.html'
    success_url = reverse_lazy('index')


    