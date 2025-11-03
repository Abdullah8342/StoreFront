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
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='review'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='review'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        unique_together = ('product','user')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.rating} - {self.user}'
