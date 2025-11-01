'''
    ProductImages
'''

from django.db import models
from .product import Product

class ProductImages(models.Model):
    '''
    Product Images
    '''
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='ProductImages/')
    alt_text = models.CharField(max_length=100,blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'product images'
        ordering = ['-is_primary','created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['product'],
                condition=models.Q(is_primary = True),
                name = 'unique_primary_image_per_unit',
            )
        ]

    def __str__(self):
        return f'Image for {self.product.name}'

    def save(self, *args,**kwargs):
        if self.is_primary:
            ProductImages.objects.filter(product = self.product,is_primary = True).update(is_primary = False)
        super().save(*args,**kwargs)
