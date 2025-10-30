'''
    ProductImages
'''

from django.db import models
from .product import Product

class ProductImages(models.Model):
    '''
    Product Images
    '''
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='ProductImages/')
    alt_text = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.name}'

