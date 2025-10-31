from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Address(models.Model):
    '''
    Address
    '''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='address'
    )
    label = models.CharField(
        max_length=50,
        blank=True,
        help_text="e.g., Home, Work, Mom's House"
    )
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\d{5}(-\d{4})?$', 'Enter a valid ZIP code.')],
    )
    country = models.CharField(max_length=50,default='Pakistan')
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Address'
        ordering = ['-is_default','-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['is_default'],
                condition = models.Q(is_default = True),
                name='unique_default_address_per_user',
            )
        ]

    def __str__(self):
        return f"{self.label or 'Address'} - {self.user.username}"


    def save(self, *args,**kwargs):
        if self.is_default:
            Address.objects.filter(user = self.user,is_default = True).update(is_default = False)
        super().save(*args,**kwargs)
