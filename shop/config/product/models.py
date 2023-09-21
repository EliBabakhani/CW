from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    price=models.DecimalField(decimal_places=2, max_digits=5)
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='static', null=True,blank=True)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='static')


    def __str__(self) -> str:
        return self.title