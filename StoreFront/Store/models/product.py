'''
    Product
'''
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.db import models
from .category import Category
from .tag import Tag


class Product(models.Model):
    '''
    Product
    '''
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=300,blank=True,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.01)])
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=150,unique=True,blank=True)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='products',
        blank=True,
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Products'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name','price']),
            models.Index(fields=['sku']),
        ]

    def __str__(self):
        return f'{self.name}'


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Product.objects.filter(slug = unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        if not self.sku:
            self.sku = f'SKU-{self.slug.upper()[:10]}-{self.id or 'NEW'}'

        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})

    def get_primary_image(self):
        return self.images.filter(is_primary = True).first() or self.images.first()
