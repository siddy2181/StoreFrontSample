from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'



class Product(models.Model):
    name=models.CharField(max_length=35)
    description = models.TextField()
    category = models.OneToOneField(Category)

    def __str__(self):
        return self.name
