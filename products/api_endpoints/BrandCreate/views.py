from rest_framework.generics import CreateAPIView

from products.models import Brand
from products.api_endpoints.BrandCreate.serializers import BrandCreateSerializer


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer
    permission_classes = []
