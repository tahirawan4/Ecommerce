from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify

from .utils import get_unique_slug


def upload_images(instance, filename):
    return '{}/{}'.format("Pictures", '%s.jpg')


class Image(models.Model):
    title = models.CharField(max_length=250)
    alt = models.CharField(max_length=250, blank=True, default='')
    slug = models.SlugField(max_length=250,unique=True)  # auto generate unique slug
    image_img = models.ImageField(upload_to=upload_images, null=True, blank=True)
    eadonly_fields = ["slug"]

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Image.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Image,self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    descrition = models.CharField(max_length=250, blank=True, default='')
    image = models.ImageField(upload_to=upload_images, null=True, blank=True)
    cat_img = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Image.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Category,self).save(*args, **kwargs)


class Slider(models.Model):
    title = models.CharField(max_length=250)
    descrition = models.CharField(max_length=250, blank=True, default='')
    slider_img = models.ImageField(upload_to=upload_images, null=True, blank=True)

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=250)
    descrition = models.CharField(max_length=250, blank=True, default='')
    product_images = models.ManyToManyField(Image)
    price = models.IntegerField()
    slug = models.SlugField(max_length=250)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to=upload_images, null=True, blank=True)
    actie_product = models.BooleanField(default=True)


    def __str__(self):
        return self.title


    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Image.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Product,self).save(*args, **kwargs)


class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.CharField(max_length=250)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.IntegerField()
    message = models.CharField(max_length=250)


    def __str__(self):
        return self.name

class SocailMedia(models.Model):
    title = models.CharField(max_length=250)
    descrition = models.CharField(max_length=250, blank=True, default='')
    image = models.ImageField(upload_to=upload_images, null=True, blank=True)
    actie_media = models.BooleanField(default=True)


    def __str__(self):
        return self.title


class TitleBar(models.Model):
    shop_title_bar_title = models.CharField(max_length=250)
    shop_title_bar = models.ImageField(upload_to=upload_images, null=True, blank=True)
    contact_title_bar_title = models.CharField(max_length=250)
    contact_title_bar = models.ImageField(upload_to=upload_images, null=True, blank=True)

class SocialLink(models.Model):
    FACEBOOK = 'facebook'
    TWITTER = 'twitter'
    INSTA = 'insta'
    LINKEDIN = 'linkedin'

    TITLE_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'twitter'),
        (INSTA, 'InstaGram'),
        (LINKEDIN, 'LinkedIn')
    )

    title = models.CharField(max_length=50, choices=TITLE_CHOICES, default=FACEBOOK, unique=True)
    font_awesome_icon_tag = models.CharField(max_length=250)
    url = models.URLField()

    def __str__(self):
        return self.title