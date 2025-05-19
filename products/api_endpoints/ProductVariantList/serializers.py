from rest_framework import serializers

from products.models import ProductVariant


class ProductVariantListSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    color_name = serializers.SerializerMethodField()
    size_name = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "name",
            "price",
            "product",
            "product_name",
            "stock",
            "color",
            "color_name",
            "size",
            "size_name",
            "is_active",
            "created_at",
            "updated_at",
        ]
    
    def get_product_name(self, obj):
        if obj.product:
            return obj.product.name
        return None
    
    def get_color_name(self, obj):
        if obj.color:
            return obj.color.name
        return None
    
    def get_size_name(self, obj):
        if obj.size:
            return obj.size.name
        return None
