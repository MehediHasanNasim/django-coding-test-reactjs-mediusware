from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.forms import VariantForm
from product.models import Variant

''' Nasim '''
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from product.serializers import *
from product.models import *
from urllib import request



class BaseVariantView(generic.View):
    form_class = VariantForm
    model = Variant
    template_name = 'variants/create.html'
    success_url = '/product/variants'


class VariantView(BaseVariantView, ListView):
    template_name = 'variants/list.html'
    paginate_by = 10

    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Variant.objects.filter(**filter_string)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context


class VariantCreateView(BaseVariantView, CreateView):
    pass


class VariantEditView(BaseVariantView, UpdateView):
    pk_url_kwarg = 'id'



'''creating api view from nasim '''
class VariantListCreate(generics.ListCreateAPIView):
    '''create customer and view list'''
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()

class VariantDetailsview(generics.RetrieveUpdateAPIView):
    '''retrieve data with pk'''
    '''update data with put method'''
    '''dele method will delete data with pk'''
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()