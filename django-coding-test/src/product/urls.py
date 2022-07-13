from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView

from product.views.variant import *
from product.views.product import *

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    # path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
    #     'product': True
    # }), name='list.product'),
    
    path('list/', product, name="list.product"),
    

    # nasim
    # variant
    path('variant_api/', VariantListCreate.as_view(), name='VariantListCreate'),
    path('variant_api/<int:pk>/', VariantDetailsview.as_view(), name='VariantDetailsview'),

    # product
    path('product_api/', ProductListCreate.as_view(), name='VariantListCreate'),
    path('product_api/<int:pk>/', ProductDetailsview.as_view(), name='VariantDetailsview'),

    # ProductImage
    path('productimage_api/', ProductImageListCreate.as_view(), name='ProductImageListCreate'),
    path('productimage_api/<int:pk>/', ProductImageDetailsview.as_view(), name='ProductImageDetailsview'),

    # ProductVariant
    path('productvariant_api/', ProductVariantListCreate.as_view(), name='ProductVariantListCreate'),
    path('productvariant_api/<int:pk>/', ProductVariantDetailsview.as_view(), name='ProductVariantDetailsview'),

    # ProductVariantPrice
    path('productvariantprice_api/', ProductVariantPriceListCreate.as_view(), name='ProductVariantPriceListCreate'),
    path('productvariantprice_api/<int:pk>/', ProductVariantPriceDetailsview.as_view(), name='ProductVariantPriceDetailsview'),

]
