from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic

from eCommerce import settings

from django.shortcuts import render, redirect

from ecommerce.forms import ContactForm, ContactForm_2
from ecommerce.models import Slider, Product, SocailMedia, Category, TitleBar, SocialLink
from django.core.mail import BadHeaderError, send_mail


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        slider_images = Slider.objects.all()
        products = Product.objects.all()
        social_media = SocailMedia.objects.all()
        category = Category.objects.all()[:9]
        social_links = SocialLink.objects.all()

        return render(request, self.template_name,
                      {'social_links':social_links,'category':category, 'slider_images': slider_images, 'products': products, 'social_media': social_media})


class CategoryProductsView(generic.TemplateView):
    template_name = 'categoryProducts.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.all()[:6]
        social_links = SocialLink.objects.all()
        return render(request, self.template_name, {'social_links':social_links,'category':category,'products': products})


class InterestedProducts(generic.TemplateView):
    template_name = 'product.html'

    def post(self, request):
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                msg = form.cleaned_data['message']
                name = form.cleaned_data['name']
                bookId = form.cleaned_data['bookId']
                product_name = form.cleaned_data['product_name']

                message ="product_name: "+ product_name+ "\n" +"id: " + bookId + "\n" + "Name: " + name + "\n" + "From: " + from_email + "\n" + "Subject: " + subject + "\n" + "Message: " + msg
                try:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER, ],
                              fail_silently=False, )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('index')
        return render(request, "product.html", {'form': form})

class ProductsView(generic.TemplateView):
    template_name = 'product.html'

    def get(self, request, *args, **kwargs):
        title_bar = TitleBar.objects.all()[:1]
        all_products = Product.objects.all()
        category = Category.objects.all()[:6]
        social_links = SocialLink.objects.all()
        return render(request, self.template_name, {'social_links':social_links,'category':category,'all_products':all_products,'title_bar':title_bar})


class ProductDetailView(generic.TemplateView):
    template_name = 'product-detail.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        products = Product.objects.filter(slug=slug).first()
        newarrivals = Product.objects.all()
        category = Category.objects.all()[:6]
        social_links = SocialLink.objects.all()
        return render(request, self.template_name,{'newarrivals':newarrivals,'social_links':social_links,'category':category,'products': products})


class ContactView(generic.TemplateView):
    template_name = 'contact.html'
    title_bar = TitleBar.objects.all()[:1]

    def get(self, request, *args, **kwargs):
        title_bar = TitleBar.objects.all()[:1]
        category = Category.objects.all()[:6]
        social_links = SocialLink.objects.all()
        return render(request, self.template_name, {'social_links':social_links,'title_bar':title_bar,'category':category})

    def post(self, request):
        if request.method == 'GET':
            form = ContactForm_2()
        else:
            form = ContactForm_2(request.POST)
            if form.is_valid():
                phonenumber = form.cleaned_data['phonenumber']
                email = form.cleaned_data['email']
                msg = form.cleaned_data['message']
                name = form.cleaned_data['name']
                message = "Name: " + name + "\n" + "From: " + email + "\n" + "Subject: " + phonenumber + "\n" + "Message: " + msg
                try:
                    send_mail(phonenumber, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER, ],
                              fail_silently=False, )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('contact')

        return render(request, "contact.html", form)



class ModelView(generic.TemplateView):
    template_name = 'model.html'

class AboutUs(generic.TemplateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()[:6]
        social_links = SocialLink.objects.all()
        return render(request, self.template_name,{'social_links':social_links,'category':category})
