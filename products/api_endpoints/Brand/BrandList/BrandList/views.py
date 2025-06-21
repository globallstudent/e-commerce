from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Brand
from products.api_endpoints.BrandList.serializers import BrandListSerializer


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)


class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = []
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)