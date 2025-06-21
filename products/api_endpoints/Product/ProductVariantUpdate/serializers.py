from rest_framework import serializers

from products.models import ProductVariant


class ProductVariantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "name",
            "price",
            "product",
            "stock",
            "color",
            "size",
            "is_active",
        ]
