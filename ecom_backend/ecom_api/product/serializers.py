from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True)

    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'description',
                  'image', 'is_active', 'created_at', 'updated_at')
