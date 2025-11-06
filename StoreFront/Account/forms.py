from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import AbstractUser

class CustomUserCreatingForm(UserCreationForm):
    '''
    Docstring for CustomUserCreatingForm
    '''
    class Meta(UserCreationForm.Meta):
        '''
        Docstring for Meta
        '''
        model = AbstractUser
        fields = UserCreationForm.Meta.fields+ ('email','first_name','last_name')
