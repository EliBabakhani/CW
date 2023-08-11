from django.shortcuts import render
from django.views import View
from .models import Todo
from .mixins import *


class IndexView(View):
    def get(self, request):
        return render(request, 'Home/index.html')


class TodoListView(View):
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, 'Home/todo_list.html', {'todos': todos})


class TodoDetailView(TodoMixin, View):
    template_name = 'Home/todo_detail.html'


class ProfileView(ProfileMixin,View):
    template_get=""
    template_post=""
    template_name='Home/profile.html'


