from django.db import models
from django.conf import settings
from Profile.models import Address
# from .payment import Payment

class Order(models.Model):
    '''
    Order
    '''
    ORDER_STATUS = [
        ('P','Pending'),
        ('S','Shipped'),
        ('D','Delivered'),
        ('C','Cancelled'),
    ]
    PAYMENT_METHOD = [
        ('O','Other')
    ]
    status = models.CharField(choices=ORDER_STATUS,default='P')
    total_ammount = models.DecimalField(decimal_places=2,max_digits=8)
    payment_method = models.TextField(choices=PAYMENT_METHOD,default='O')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order')
    address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='order')
    # payment = models.ForeignKey(Payment,on_delete=models.CASCADE,related_name='order')
