from __future__ import unicode_literals
from django.db import models


def upload_images(instance, filename):
    return '{}/{}'.format("Pictures", '%s.jpg')


class Image(models.Model):
    title = models.CharField(max_length=250)
    alt = models.CharField(max_length=250, blank=True, default='')
    slug = models.SlugField(max_length=250)  # auto generate unique slug
    image_img = models.ImageField(upload_to=upload_images, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    descrition = models.CharField(max_length=250, blank=True, default='')
    cat_img = models.ManyToManyField(Image)

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=250)
    descrition = models.CharField(max_length=250, blank=True, default='')
    slider_img = models.ImageField(upload_to=upload_images, null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=250)
    descrition = models.CharField(max_length=250, blank=True, default='')
    product_img = models.ManyToManyField(Image)
    price = models.IntegerField()
    slug = models.SlugField(max_length=250)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
