from __future__ import unicode_literals

from django.contrib import admin
# from django.db import models

from ecommerce.models import Slider, Image ,Category,Product, ContactUs, Order, SocailMedia, TitleBar,SocialLink

class SocialLinkAdmin(admin.ModelAdmin):
    model = SocialLink

class TitleBarAdmin(admin.ModelAdmin):
    model = TitleBar
    list_display = ('shop_title_bar_title','shop_title_bar')

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('title', 'descrition', 'price')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('title', 'descrition')
    prepopulated_fields = {'slug': ('title',)}

class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ('title', 'descrition')

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('title','alt')
    prepopulated_fields = {'slug': ('title',)}

class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ('name','phone','email','message')

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('name', 'email' ,'phone', 'message')

class SocailMediaAdmin(admin.ModelAdmin):
    model = SocailMedia
    list_display = ('title', 'descrition')


admin.site.register(SocailMedia, SocailMediaAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(TitleBar,TitleBarAdmin)
admin.site.register(SocialLink,SocialLinkAdmin)




