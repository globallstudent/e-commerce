from rest_framework import serializers

from products.models import Brand


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "name",
            "slug",
            "logo",
            "created_at",
            "updated_at",
        ]
