from django.db import models
from account.models import User
from product.models import Product

class Order( models.Model):
    cutomer=models.ForeignKey(User, on_delete=models.PROTECT)
    discount=models.ForeignKey('Discount', on_delete=models.CASCADE)
    payment=models.ForeignKey('Payment', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.cutomer

class OredrItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unit_price=models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self) -> str:
        return self.order

class Discount(models.Model):
    discount=models.DecimalField(decimal_places=2, max_digits=5)

class Payment(models.Model):
    is_paid=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.is_paid