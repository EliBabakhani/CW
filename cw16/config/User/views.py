from django.shortcuts import render
from .models import CustomUser
from django.shortcuts import get_list_or_404

def user_tasks(request):
    all_users=get_list_or_404(CustomUser)
    return render(request, 'User/all_users.html', {'all_users': all_users})


def user_login(request):
    if request.method=="POST":
        cd=request.POST(CustomUser)
        if cd.is_valid():
            pass
    else:
        form=
            
    
