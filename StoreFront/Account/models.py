'''
Account.Models
'''
from django.db import models
from django.contrib.auth.models import AbstractUser as AU
# Create your models here.

class AbstractUser(AU):
    '''
    Custom User Model
    '''
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username}'
