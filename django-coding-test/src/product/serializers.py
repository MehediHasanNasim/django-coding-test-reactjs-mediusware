from rest_framework import serializers
from .models import *


class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Variant

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Product
        
class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = ProductImage

class ProductVariantSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = ProductVariant

class ProductVariantPriceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = ProductVariantPrice