from django.db import models
from Author.models import *



class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date=models.DateTimeField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title



class Comment(models.Model): 
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    content=models.TextField()
    date=models.DateTimeField()

    def __str__(self) -> str:
        return self.content

