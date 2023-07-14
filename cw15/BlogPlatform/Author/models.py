from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    photo = models.ImageField(upload_to='images', default='images/unknown.jpg')
    def __str__(self) -> str:
        return self.name