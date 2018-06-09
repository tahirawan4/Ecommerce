# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from eCommerce import settings

from django.shortcuts import render

from ecommerce.models import Slider


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        slider_images = Slider.objects.all()

        return render(request, self.template_name, {'slider_images': slider_images})

class ProductsView(generic.TemplateView):
    template_name = 'product.html'

class ProductDetailView(generic.TemplateView):
    template_name = 'product-detail.html'

class ContactView(generic.TemplateView):
    template_name = 'contact.html'