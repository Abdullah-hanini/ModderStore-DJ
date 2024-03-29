import datetime
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models import Min

from accounts.models import Profile



status = (
    ('Payment Pending','Payment Pending'),
    ('Payment Canceled','Payment Canceled'),
    ('Processing','Processing'),
    ('Completed','Completed'),
)


def imgup (instance,fname) :
    imagename , extension = fname.split(".")
    return "games/%s.%s"%(instance.id,extension)

class Products(models.Model):
    is_hidden = models.BooleanField(default=False)
    is_ent = models.BooleanField(default=False)
    related_products = models.ManyToManyField('self', blank=True, symmetrical=False)
    title = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=100)
    email = models.EmailField()
    phonen = models.CharField(max_length=15)
    products = models.ManyToManyField(Products, through='OrderItem')
    total= models.DecimalField(max_digits=8, decimal_places=2)
    ostatus = models.CharField(max_length=50,choices=status,default='Payment Pending')
    pdiscrption = models.TextField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)

    

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)