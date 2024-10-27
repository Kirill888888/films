from django.shortcuts import render
from .models import Movie
# Create your views here.


def movies(request):
    films = Movie.objects.all()
    return render(request, 'cinema/movies.html', {'films':films})
