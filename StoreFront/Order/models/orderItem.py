from Store.models import Product
from django.db import models
from .order import Order


class OrderItem(models.Model):
    '''
    OrderItem
    '''
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderItem')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='orderItem')
