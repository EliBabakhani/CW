from django.db import models
from User.models import Users

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    due_date=models.DateTimeField()
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    tags=models.ForeignKey('Tag',on_delete=models.CASCADE)
    status_field=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.title}\t{self.description[:10]}'

class Category(models.Model):
    name=models.CharField(max_length=50)
    task=models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
