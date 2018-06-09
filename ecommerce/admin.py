from __future__ import unicode_literals

from django.contrib import admin

from models import Slider, Image ,Category,Product

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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Image, ImageAdmin)





