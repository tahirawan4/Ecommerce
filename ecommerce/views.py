# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic

from eCommerce import settings

from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm
from ecommerce.models import Slider,Product, SocailMedia



from django.core.mail import send_mail




class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        slider_images = Slider.objects.all()
        products = Product.objects.all()
        social_media = SocailMedia.objects.all()
        return render(request, self.template_name, {'slider_images': slider_images, 'products':products, 'social_media':social_media})

class ProductsView(generic.TemplateView):
    template_name = 'product.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name, {'products':products})


class ProductDetailView(generic.TemplateView):
    template_name = 'product-detail.html'

class ContactView(generic.TemplateView):
    template_name = 'contact.html'

class ModelView(generic.TemplateView):
    template_name = 'model.html'

class ContactUsView(generic.TemplateView):
    template_name = 'ContactUs.html'

    def post(self, request):
        # import pdb;pdb.set_trace()
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                msg = form.cleaned_data['message']
                name = form.cleaned_data['name']
                # message = 'This is message'
                message = "Name: " + name + "\n" + "From: " + from_email + "\n" + "Subject: " + subject + "\n" + "Message: " + msg
                try:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER, ],
                              fail_silently=False, )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('contactus')
        # context = get_base_data()
        # context['form'] = form
        return render(request, "contactUs.html", form)