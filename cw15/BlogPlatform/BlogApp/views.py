from django.shortcuts import render, get_object_or_404,get_list_or_404
from .models import *

def post_list(request):
    all_post=Post.objects.all()
    return render(request, 'BlogApp/post_list.html', {'post': all_post})

def post_details(request, pk):
    post=Post.objects.get(pk=pk)
    return render(request, 'BlogApp/post_details.html', {'post': post})

def home(request):
    return render(request, 'BlogApp/home.html')

def category_list(request):
    all_category=Category.objects.all()
    return render(request, 'BlogApp/category_list.html', {'category': all_category})

def category_details(request,id):
    category=Category.objects.get(pk=id)
    return render(request, 'BlogApp/category_details.html', {'category': category})
