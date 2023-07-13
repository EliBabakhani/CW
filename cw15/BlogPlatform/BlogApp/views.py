from django.shortcuts import render
from . import models

def post_list(request):
    all_post=models.Post.objects.all()
    return render(request, 'BlogApp/post_list.html', {'post': all_post})

def post_details(request, pk):
    post=models.Post.objects.get(pk=post.id)
    return render(request, 'BlogApp/post_details', post)
def home(request):
    