from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User




'''
Editions = (
    ('Standard Edtion','Standard Edtion'),
    ('Deluxe Edtion','Deluxe Edtion'),
    ('Ultimate Edtion','Ultimate Edtion'),

)
'''

def imgup (instance,fname) :
    imagename , extension = fname.split(".")
    return "games/%s.%s"%(instance.id,extension)

class Products(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to=imgup)
    discription = models.TextField(max_length=100000)
    Sdiscription = models.CharField(max_length=100)
    price = models.FloatField(max_length=40)
    stock = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Products,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name   

class Orders(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
