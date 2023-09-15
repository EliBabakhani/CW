from django.db import models
class Order( models.Model):
    cutomer=models.ForeignKey(User, on_delete=models.PROTECT)
    discount=models.ForeignKey('Discount', on_delete=models.CASCADE)
    payment=models.ForeignKey('Payment', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.cutomer

class OredrItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=10)
    unit_price=models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self) -> str:
        return self.order
