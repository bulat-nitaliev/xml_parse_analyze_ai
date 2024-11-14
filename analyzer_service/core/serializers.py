from rest_framework import serializers
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 
                  'date_product', 
                  'quantity',
                  'price',
                  'category'
                )