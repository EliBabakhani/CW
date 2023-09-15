from django.db import models
class Order( models.Model):
    cutomer=models.ForeignKey(User, on_delete=models.PROTECT)
    discount=models.ForeignKey('Discount', on_delete=models.CASCADE)
    payment=models.ForeignKey('Payment', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.cutomer
