from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

class Cart(models.Model):
    '''
    Cart
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Cart'

    def __str__(self):
        return f'Cart of {self.user.username}'

    def get_total_item(self):
        return sum(item.quantity for item in self.cartItem.all())

    def get_total_price(self):
        return sum(item.get_subtotal() for item in self.cartItem.all())

@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_user_cart(instance,created,**kwargs):
    if created:
        Cart.objects.create(user = instance)
