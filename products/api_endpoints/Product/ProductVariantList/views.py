from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import ProductVariant
from products.api_endpoints.ProductVariantList.serializers import ProductVariantListSerializer


class ProductVariantListAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)


class ProductVariantRetrieveAPIView(RetrieveAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer
    permission_classes = []
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)
