from django.shortcuts import render
import random

# Create your views here.
def index(request):
    eightball = open('eightball/eightball.txt').readlines()
    return render(request, 'eightball/index.html', {'eightball': eightball[random.randint(0, len(eightball) - 1)]})