from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    '''
    Profile
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    bio = models.TextField(
        blank=True,
        max_length=500,
        help_text='Short Bio or description'
    )

    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_pictures/'
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text="e.g., +1234567890"
    )

    dob = models.DateField(
        null=True,
        blank=True,
        help_text='Optional for Birthday offers'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Profile'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_full_name(self):
        return self.user.get_full_name() or self.user.username


@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user =  instance)



@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def save_user_profile(sender,instance,**kwargs):
    if hasattr(instance,'profile'):
        instance.profile.save()
