from django.db import models
from django.conf import settings
from Store.models import Product

class WishList(models.Model):
    '''
    WishList
    '''
    product = models.ManyToManyField(Product,related_name='wishlist')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist'
    )

    def __str__(self):
        return f'{self.user.username}'
