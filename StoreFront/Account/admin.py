'''
Decorators
'''
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import AbstractUser
# Register your models here.



class CustomUserAdmin(UserAdmin):
    '''
    Docstring for CustomUserAdmin
    '''
    model = AbstractUser
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    'email',
                    'first_name',
                    'last_name',
                    "usable_password",
                    "password1",
                    "password2"
                ),
            },
        ),
    )


admin.site.register(AbstractUser,CustomUserAdmin)
