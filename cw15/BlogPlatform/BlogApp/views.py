from django.shortcuts import render
from . import models

def post_list(request):
    all_post=models.Post.object.all()
    return render(request, 'post_list.html', {'post': all_post})

def post_details(request, pk):
    pass