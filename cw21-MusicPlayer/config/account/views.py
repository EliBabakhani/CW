from typing import Any
from django import http
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserLoginForm
from django.views.generic import View,CreateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User
from music.models import Song,PlayList
from django.contrib.auth.mixins import LoginRequiredMixin


class UserLoginView(View):
    form_class=UserLoginForm
    def dispatch(self, request, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return redirect('home:index')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        form=self.form_class()
        return render(request,'account/user_login.html', context={'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'Logged in successfully', 'success')
                return redirect('home:index')
            messages.error(request,'there is Error', 'danger')
            return render(request, 'account/usr')
        
class UserRegisterView(CreateView):
    model=User
    fields=['username', 'password','image','account_type']
    template_name='account/user_register.html'
    success_url='login'

    def dispatch(self, request, *args: Any, **kwargs: Any) :
        if request.user.is_authenticated:
            return redirect('home:index')
        print('hi')
        return super().dispatch(request, *args, **kwargs) 
    
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)


class UserLogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'logged out successfully', 'success')
            return redirect('home:index')


class UserProfileView(LoginRequiredMixin,View):    
    def get(self, request,id):
        user=User.objects.get(id=id)
        playlist=PlayList.objects.all(owner=user)
        return render(request,'account/user_profile.html', context={'playlist':playlist})
    


