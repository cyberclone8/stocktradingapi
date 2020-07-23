from django.db import models


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=4)


class Order(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='name')
    quantity = models.IntegerField()

    @property
    def value(self, stock, quantity):
        return stock.price * quantity
