# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from eCommerce import settings

from django.shortcuts import render

from ecommerce.models import Slider,Product, SocailMedia


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        slider_images = Slider.objects.all()
        products = Product.objects.all()
        social_media = SocailMedia.objects.all()
        return render(request, self.template_name, {'slider_images': slider_images, 'products':products, 'social_media':social_media})

class ProductsView(generic.TemplateView):
    template_name = 'product.html'

class ProductDetailView(generic.TemplateView):
    template_name = 'product-detail.html'

class ContactView(generic.TemplateView):
    template_name = 'contact.html'