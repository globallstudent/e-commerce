from rest_framework.generics import CreateAPIView

from products.models import ProductVariant
from products.api_endpoints.ProductVariantCreate.serializers import ProductVariantCreateSerializer


class ProductVariantCreateAPIView(CreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantCreateSerializer
    permission_classes = []
