from django.db import models
from Order.models import Order

PAYMENT_STATUS = [
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('failed', 'Failed'),
    ('refunded', 'Refunded'),
]

class Payment(models.Model):
    '''
    Payment
    '''
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payment')
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    transaction_id = models.CharField(max_length=100,blank=True,null=True,unique=True)
    gateway = models.CharField(max_length=20,default='strip')
    status = models.CharField(max_length=20,choices=PAYMENT_STATUS,default='pending')
    paid_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name = 'Payment'
        ordering = ['-created_at']

    def __str__(self):
        return f'Payment {self.transaction_id or 'N/A'}-{self.order}'
