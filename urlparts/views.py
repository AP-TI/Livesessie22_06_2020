from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, path):
    if '//' in path or path[0] == '/': return HttpResponse('Ongeldige url!')
    parts = path.split('/')
    return render(request, 'urlparts/index.html', {'parts': parts})