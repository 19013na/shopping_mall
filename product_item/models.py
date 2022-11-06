from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Publisher(models.Model):
    author = models.CharField(max_length=10)
    publisher = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(null=True)
    page = models.IntegerField(null=True)
    image = models.ImageField(upload_to='product_item/images/%Y/%m/%d/', blank=True)
    price = models.IntegerField()

    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)
