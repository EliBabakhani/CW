from typing import Any, List, Tuple
from django.contrib import admin
from .models import *
from MyTasks.models import Task



from django.contrib import admin


class IsGreatUserFilter(admin.SimpleListFilter):
    title = 'Great'
    parameter_name = 'is_great_user'

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [('is_great_user','Great')]

    def queryset(self, request, queryset):
        if self.value() == 'is_great_user':
            return queryset.filter(is_great_user=True)



@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','is_active','number_of_task','is_great_user']

    @admin.display(ordering='username')
    def number_of_task(self,user):
        query=Task.objects.filter(user=user).count()
        print(query)
        return query
    

    def is_great_user(self,user):
        query=Task.objects.filter(user=user).count()
        if query>10:
            return True
        return False
    
    
    is_great_user.boolean=True


    