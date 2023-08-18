from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from django.shortcuts import get_list_or_404
from .forms import UserLogInForm, UserRegisterForm
from . auth import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.views import LoginView,LogoutView

def user_tasks(request):
    all_users = get_list_or_404(CustomUser)
    return render(request, 'User/all_users.html', {'all_users': all_users})


class UserLoginView(LoginView):
    authentication_form=UserLogInForm
    template_name='User/login.html'
    redirect_authenticated_user=True
    success_url='home'
    def form_valid(self, form: UserLogInForm) -> HttpResponse:
        return super().form_valid(form)

# def user_login(request):
#     if request.method == "POST":
#         form = UserLogInForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             username = cd['username']
#             password = cd['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, 'Data were wrong')
#     else:
#         form = UserLogInForm()
#     context = {'form': form}
#     return render(request, 'User/login.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            # user = CustomUser(cd['username'], cd['email'], cd['password'])
            form.save()
            return redirect('home')


    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'User/userregister.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

