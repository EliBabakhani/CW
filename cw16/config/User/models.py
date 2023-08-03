from django.db import models

class Users(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images', default='images/unknown.png')

    def __str__(self) -> str:
        return self.name

