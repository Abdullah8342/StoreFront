from django.db import models
from .order import Order

class Payment(models.Model):
    '''
    Payment
    '''
    PAYMENT_STATUS = [
        ('S','Success'),
        ('F','Faild'),
    ]
    ammount = models.DecimalField(max_digits=8,decimal_places=2)
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name='payment')
    transaction_id = models.CharField()
    status = models.CharField(choices=PAYMENT_STATUS,max_length=1)
