from django.db import models
from djrichtextfield.models import RichTextField


class Category(models.Model):
    name = models.CharField('Category name', max_length=25, unique=True)
    description = RichTextField('Description', blank=True)
    activate = models.BooleanField('Active', default=False)
    created = models.DateTimeField('Created', auto_now=True)
    updated = models.DateTimeField('Updated', auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
