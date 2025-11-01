'''
Tag
'''
from django.utils.text import slugify
from django.db import models

class Tag(models.Model):
    '''
    Tag
    '''
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tag'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Tag.objects.filter(slug = unique_slug).exists():
                unique_slug = f'{self.name}-{counter}'
                counter += 1
            self.slug = unique_slug
        super().save(*args,**kwargs)
