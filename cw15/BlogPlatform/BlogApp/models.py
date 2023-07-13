from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=100)
    publication_date=models.DateTimeField()

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

class Comment(models.Model): 
    post=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField()

class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()