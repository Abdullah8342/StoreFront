'''
Tag
'''
from django.db import models
from .product import Product

class Tag(models.Model):
    '''
    Tag
    '''
    product = models.ManyToManyField(Product,related_name='tags')
    name = models.CharField(unique=True)


    def __str__(self):
        return f'{self.name}'
