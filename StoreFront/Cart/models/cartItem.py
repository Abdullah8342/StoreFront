from django.db import models
from .cart import Cart
from Store.models import Product

class CartItem(models.Model):
    '''
    CartItem
    '''
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartItem')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'
