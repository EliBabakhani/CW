from django.shortcuts import render
from . import models

def post_list(request):
    all_post=models.Post.objects.all()
    return render(request, 'BlogApp/post_list.html', {'post': all_post})

def post_details(request, pk):
    post=models.Post.objects.get(pk=pk)
    return render(request, 'BlogApp/post_details.html', {'post': post})

def home(request):
    return render(request, 'BlogApp/home.html')

def author_list(request):
    all_author=models.Author.objects.all()
    return render(request, 'BlogApp/author_list.html', {'author': all_author})
