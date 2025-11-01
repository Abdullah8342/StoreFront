'''
    Category
'''

from django.utils.text import slugify
from django.urls import reverse
from django.db import models


class Category(models.Model):
    '''
    Category
    '''
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=120,unique=True,blank=True)
    description = models.TextField(blank=True)
    parents = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subcategories',
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Category.objects.filter(slug = self.slug).exists():
                unique_slug = f'{self.name}-{counter}'
                counter += 1
            self.slug = unique_slug
        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})


    def get_breadcrumb(self):
        breadcrumb = [self]
        category = self
        while category.parents:
            category = category.parents
            breadcrumb.insert(0,category)
        return breadcrumb
