from django.db import models
from django.conf import settings

class Cart(models.Model):
    '''
    Cart
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username}'
