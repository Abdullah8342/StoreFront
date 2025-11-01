from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from Store.models import Product
from django.db import models
from .cart import Cart

class CartItem(models.Model):
    '''
    CartItem
    '''
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cartItem'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    added_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'CartItem'
        ordering = ['-added_at']
        unique_together = ['cart','product']

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


    def clean(self):
        if self.quantity > self.product.stock:
            raise ValidationError(
                f'Only {self.product.stock} in Stock \n'
                f'Cannot add {self.quantity}'
            )

    def get_subtotal(self):
        return self.quantity * self.product.price
