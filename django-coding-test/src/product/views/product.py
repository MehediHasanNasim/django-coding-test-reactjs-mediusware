from django.views import generic
from product.forms import ProductForm

from product.models import Variant, Product

''' Nasim '''
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from product.serializers import *
from product.models import *
from urllib import request

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# class BaseProductView(generic.View):
#     form_class = ProductForm
#     model = Product
#     template_name = 'products/create.html'
#     success_url = '/product/products'

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
    
    
# rafffff
# class ProductView(BaseProductView, ListView):
#     template_name = 'products/list.html'
#     paginate_by = 3

#     def get_queryset(self):
#         filter_string = {}
#         print(self.request.GET)
#         for key in self.request.GET:
#             if self.request.GET.get(key):
#                 filter_string[key] = self.request.GET.get(key)
#         return Product.objects.filter(**filter_string)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product'] = True
#         context['request'] = ''
#         if self.request.GET:
#             context['request'] = self.request.GET['title__icontains']
#         return context

# nasim
def product(request):
    product = Product.objects.all()

    product = {
        'product': product
    }
    return render(request, 'products/list.html', product)




'''creating api view from nasim '''
# product
# @method_decorator(csrf_exempt, name='dispatch')
class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetailsview(generics.RetrieveUpdateAPIView):
    '''retrieve data with pk'''
    '''update data with put method'''
    '''dele method will delete data with pk'''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
# product image

class ProductImageListCreate(generics.ListCreateAPIView):
    '''create customer and view list'''
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()

class ProductImageDetailsview(generics.RetrieveUpdateAPIView):
    '''retrieve data with pk'''
    '''update data with put method'''
    '''dele method will delete data with pk'''
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    
# Product Variant

class ProductVariantListCreate(generics.ListCreateAPIView):
    '''create customer and view list'''
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all()

class ProductVariantDetailsview(generics.RetrieveUpdateAPIView):
    '''retrieve data with pk'''
    '''update data with put method'''
    '''dele method will delete data with pk'''
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all()
    
# Product variant price

class ProductVariantPriceListCreate(generics.ListCreateAPIView):
    '''create customer and view list'''
    serializer_class = ProductVariantPriceSerializer
    queryset = ProductVariantPrice.objects.all()

class ProductVariantPriceDetailsview(generics.RetrieveUpdateAPIView):
    '''retrieve data with pk'''
    '''update data with put method'''
    '''dele method will delete data with pk'''
    serializer_class = ProductVariantPriceSerializer
    queryset = ProductVariantPrice.objects.all()