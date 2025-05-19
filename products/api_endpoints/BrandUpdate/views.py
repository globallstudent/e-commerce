from rest_framework.generics import UpdateAPIView

from products.models import Brand
from products.api_endpoints.BrandUpdate.serializers import BrandUpdateSerializer


class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer
    permission_classes = []
    lookup_field = 'pk'
