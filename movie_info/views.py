from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.

def index(request) :
    return render(request, 'movie_info/home.html')

def movieInfo(request, movie_id) :
    context = {"id":movie_id}
    return render(request, 'movie_info/infoMovie.html', context)