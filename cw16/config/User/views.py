from django.shortcuts import render
from .models import Users
from django.shortcuts import get_list_or_404

def user_tasks(request):
    all_users=get_list_or_404(Users)
    return render(request, 'User/all_users.html', {'all_users': all_users})
