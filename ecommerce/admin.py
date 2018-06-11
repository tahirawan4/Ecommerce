from __future__ import unicode_literals

from django.contrib import admin

from models import Slider, Image ,Category,Product, ContactUs, Order, SocailMedia


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('title', 'descrition', 'price', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('title', 'descrition')

class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ('title', 'descrition')

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('title','alt','slug')

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




