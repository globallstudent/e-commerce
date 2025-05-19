from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Product
from products.api_endpoints.ProductList.serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer
    permission_classes = []
