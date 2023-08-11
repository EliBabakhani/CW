from django.shortcuts import render, redirect
from .models import Task
from .forms import *

   

class TodoOwnerRequiredMixin:
    form_class = MyTaskForm
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        todo = Task.objects.get(id=kwargs['id'])
        if not todo.user == request.user:
            return redirect ('login')
        return super(TodoOwnerRequiredMixin, self).dispatch(request, *args, **kwargs)


    def get(self, request, id):
        todo = Task.objects.get(id=id)
        return render(request, self.template_name, {'todo': todo})

    def post(self, request, id):
        todo = Task.objects.get(id=id)
        form = self.form_class(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'todo': todo})


class ProfileMixin:
    form_class=ProfileForm
    
    def dispatch(self, request, *args, **kwargs):
        profile = Task.objects.get(id=kwargs['id'])
        if not profile.is_authenticated():
            return redirect("log_in")
        return super(ProfileMixin, self).dispatch(request, *args, **kwargs)

    def get(self, request,id):
        profile=Task.objects.get(id=id)
        return render(request, self.template_name,{"profile":profile})
    
    def post(self, request,id):
        profile=Task.objects.get(id=id)
        form=self.form_class(request.POST, isinstance=profile)
        if form.is_valid():
            profile.save()
            return redirect('thank_you')
        return render(request, self.template_name, {'profile': profile})
