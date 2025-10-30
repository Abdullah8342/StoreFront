from django.db import models
from django.conf import settings

class Profile(models.Model):
    '''
    Profile
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(blank=True,null=True,upload_to='profile_pictures/')
    phone_number = models.CharField(max_length=11)
    dob = models.DateField(null=True,blank=True)


    def __str__(self):
        return f'{self.user.username}'
