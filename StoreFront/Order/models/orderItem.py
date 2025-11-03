from django.core.validators import MinValueValidator
from Store.models import Product
from django.db import models
from .order import Order


class OrderItem(models.Model):
    '''
    OrderItem
    '''
    quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Product price when order was placed'
    )
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderItem')
    product = models.ForeignKey(Product,on_delete=models.RESTRICT,related_name='orderItem')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order Item'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


    def get_subtotal(self):
        return self.quantity * self.price
