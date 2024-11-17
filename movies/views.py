from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from movies.utils.movies import get_all_movies

def movies(request):
    movies_info = get_all_movies()
    return render(request, 'movies/main.html', {'movies': movies_info})
    