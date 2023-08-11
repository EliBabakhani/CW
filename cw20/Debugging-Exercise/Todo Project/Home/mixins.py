from django.shortcuts import render, redirect
from .models import Todo,User
from .forms import *
from django.core.exceptions import PermissionDenied



class TodoMixin:
    form_class = TodoForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['id'])
        if not todo.user == request.user:
            raise PermissionDenied
        return super(TodoMixin, self).dispatch(request, *args, **kwargs)


    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        return render(request, self.template_name, {'todo': todo})

    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})
    

class TodoOwnerRequiredMixin:
    form_class = UpdateForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['id'])
        if not todo.user == request.user:
            raise PermissionDenied
        return super(TodoOwnerRequiredMixin, self).dispatch(request, *args, **kwargs)


    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        return render(request, self.template_name, {'todo': todo})

    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})


class ProfileMixin:
    form_class=ProfileForm
    template_name=None
    
    def dispatch(self, request, *args, **kwargs):
        profile = User.objects.get(id=kwargs['id'])
        if not profile.is_authenticated():
            return redirect("log_in")
        return super(ProfileMixin, self).dispatch(request, *args, **kwargs)

    def get(self, request,id):
        profile=User.objects.get(id=id)
        return render(request, self.template_name,{"profile":profile})
    
    def post(self, request,id):
        profile=User.objects.get(id=id)
        form=self.form_class(request.POST, isinstance=profile)
        if form.is_valid():
            profile.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'profile': profile})
