from rest_framework.generics import UpdateAPIView

from products.models import Product
from products.api_endpoints.ProductUpdate.serializers import ProductUpdateSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = []
    lookup_field = 'pk'
