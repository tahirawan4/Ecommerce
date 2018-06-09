# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='images',
            new_name='cat_img',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_img',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='image',
            new_name='slider_img',
        ),
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ManyToManyField(to='ecommerce.Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='ecommerce.Category'),
        ),
    ]