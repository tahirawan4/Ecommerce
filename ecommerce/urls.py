from django.conf.urls import url
from ecommerce import views
from ecommerce.views import IndexView, CategoryProductsView, ProductDetailView, ContactView, ModelView, ProductsView, \
    InterestedProducts, AboutUs

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
                # url(r'^blog/(?P<slug>[\w-]+)/$', 'myapp.views.blog_detail', name='blog_detail'),
    url(r'^productcategory/(?P<slug>[\w-]+)/$', CategoryProductsView.as_view(), name='category_product'),

    # url(r'^productcategory/(?P<cid>\d+)/$', CategoryProductsView.as_view(), name='category_product'),
    url(r'^products/$', ProductsView.as_view(), name='product'),
    url(r'^product_detail/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^model/$', ModelView.as_view(), name='model'),
    url(r'^interested/$', InterestedProducts.as_view(), name='interested_products'),
    url(r'^about/$', AboutUs.as_view(), name='about')

]
