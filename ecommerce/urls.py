from django.conf.urls import url
from ecommerce import views
from ecommerce.views import IndexView, ProductsView, ProductDetailView, ContactView, ModelView

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^products/$', ProductsView.as_view(), name='product'),
    url(r'^product_detail/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^model/$', ModelView.as_view(), name='model')


]
