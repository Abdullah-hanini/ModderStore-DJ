from django.db import models

from products.models import Products

class hot_pro (models.Model):
    product = models.ManyToManyField(Products, blank=True, symmetrical=False)

class entertainment (models.Model):
    product = models.ManyToManyField(Products, blank=True, symmetrical=False)

