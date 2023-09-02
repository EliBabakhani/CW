from typing import Any
from django import http
from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegisterForm
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User
from music.models import Song,PlayList
from django.contrib.auth.mixins import LoginRequiredMixin

# • Authentication views (login, signup, logout).
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
        
class UserRegisterView(View):
    form_class=UserRegisterForm

    def dispatch(self, request, *args: Any, **kwargs: Any) :
        if request.user.is_authenticated:
            return redirect('home:index')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        form=self.form_class
        return render(request, 'account/user_register.html', context={'form':form})
    
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(username=cd['username'], password=cd['password'], image=cd['file'], account_type=cd['account_type'])
            messages.success(request,'Registered successfully', 'success')
            return redirect('home:index')
        messages.error(request, 'Registered failed','danger')
        return redirect('account:user_register')


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
        return render(request,'account/profile.html', context={'playlist':playlist})
