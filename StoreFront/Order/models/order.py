from django.core.validators import MinValueValidator
from django.db import models
from Store.models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from Profile.models import Address
import uuid # universal unique identifier


ORDER_STATUS = [
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
    ('refunded', 'Refunded'),
]
class Order(models.Model):
    '''
    Order
    '''
    status = models.CharField(max_length=20,choices=ORDER_STATUS,default='pending')
    total_ammount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )
    order_number = models.CharField(max_length=20,unique=True,editable=False)
    shipping_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        related_name='shipping_orders'
    )
    billing_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        related_name='billing_address'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Order'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['order_number']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f'Order {self.order_number} - {self.user.username}'



    def _generate_order_number(self):
        return f'ORD-{uuid.uuid4().hex.upper()[:8]}'

    def save(self,*args,**kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args,**kwargs)


    def get_total_items(self):
        return sum(item.quantity for item in self.orderItem.all())


    def get_total_price(self):
        return sum(item.price for item in self.orderItem.all())


@receiver(post_save,sender = Order)
def update_stock_product(sender,instance,created,**kwargs):
    if not created and instance.status in ['processing','shipped']:
        for item in instance.items.all():
            product = item.product
            if product.stock >= item.quantity:
                product.stock -= item.quantity
                product.save()
            else:
                pass
