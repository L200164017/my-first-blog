from django.shortcuts import render
from django.http import HttpResponse
import pandas as pa
import matplotlib as plot

# Create your views here.

def home(request):
    return HttpResponse('<h1>Blogging</h1>')


def about(request):
        return HttpResponse('<h1>Bloging About</h1>')

    
