from django.db import models
from django.conf import settings

class Address(models.Model):
    '''
    Address
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    is_default = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username}'
