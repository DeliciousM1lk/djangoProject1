from django.views import View
from django.shortcuts import *
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from .form import FilmForm

class FilmListView(View):
    def get(self, request):
        all_films = Film.objects.all()
        context = {'all_films': all_films}
        return render(request, 'films/films.html', context)

class FilmDetailBySlugView(View):
    def get(self, request, slug):
        film = get_object_or_404(Film, slug=slug)
        context = {'film': film}
        return render(request, 'films/film.html', context)

class FilmDetailByIdView(View):
    def get(self, request, pk):
        film = get_object_or_404(Film, pk=pk)
        context = {'film': film}
        return render(request, 'films/film.html', context)

class FilmCreateView(View):
    def get(self, request):
        form = FilmForm()
        return render(request, 'films/add_film.html', {'form': form})

    def post(self, request):
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect(reverse('films:film-by-slug', kwargs={'slug': film.slug}))
        return render(request, 'films/add_film.html', {'form': form})

class IndexView(View):
    def get(self, request):
        response = HttpResponse("Здесь будет главная страница сайта", content_type="text/plain; charset=utf-8")
        response["keywords"] = "Python Django"
        return response
