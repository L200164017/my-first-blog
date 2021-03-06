from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

import pandas as pa
import matplotlib as plot

   
# Create your views here.

def home(request):
    return HttpResponse('<h1>Blogging</h1>')


def about(request):
        return HttpResponse('<h1>Bloging About</h1>')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

    
