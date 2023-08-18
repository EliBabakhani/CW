from django.contrib import admin
from .models import *
from MyTasks.models import Task



@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','is_active','number_of_task']

    @admin.display(ordering='username')
    def number_of_task(self,user):
        query=Task.objects.filter(user=user).count()
        print(query)
        return query
        

    