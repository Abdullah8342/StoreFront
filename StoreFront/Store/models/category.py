'''
    Category
'''
from django.db import models
from .product import Product


class Category(models.Model):
    '''
    Category
    '''
    product = models.ManyToManyField(Product,related_name='category')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    slug = models.SlugField()


    def __str__(self):
        return f'{self.name}'
