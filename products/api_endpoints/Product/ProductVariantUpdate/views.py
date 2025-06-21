from rest_framework.generics import UpdateAPIView

from products.models import ProductVariant
from products.api_endpoints.ProductVariantUpdate.serializers import ProductVariantUpdateSerializer


class ProductVariantUpdateAPIView(UpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantUpdateSerializer
    permission_classes = []
    lookup_field = 'pk'
