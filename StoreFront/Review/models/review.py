from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from Store.models import Product

class Review(models.Model):
    '''
    Review
    '''
    rating = models.PositiveIntegerField(default=5,validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    comment = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='review'
    )

    def __str__(self):
        return f'{self.comment}'
