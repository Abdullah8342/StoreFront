'''
    Product
'''
from django.db import models


class Product(models.Model):
    '''
    Product
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    stock = models.PositiveIntegerField()
    sku = models.CharField(max_length=13)


    def __str__(self):
        return f'{self.name}'
