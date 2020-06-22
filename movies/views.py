from django.shortcuts import render
from django.http import HttpResponse
import redis

r = redis.Redis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)

# Create your views here.
def index(request):
    movies = []
    movieKeys = r.keys('movie:*')
    for movie in movieKeys:
        movies.append(movie[6:] + ': ' + r.get(movie))
    return render(request, 'movies/index.html', {'movies': movies})

def load(request):
    movies = open('movies/movies.txt').readlines()
    for movie in movies:
        movieSplit = movie.split(' : ')
        r.set('movie:' + movieSplit[0], movieSplit[1])
    return HttpResponse('Alle films zijn ingeladen in redis')

def search(request):
    if(request.method == "POST"):
        movies = []
        movieKeys = r.keys("movie:" + request.POST["movie"] + "*")
        for movie in movieKeys:
            movies.append(movie[6:] + ': ' + r.get(movie))
        return render(request, 'movies/index.html', {'movies': movies})
    return render(request, 'movies/search.html')