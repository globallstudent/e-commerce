from rest_framework.generics import CreateAPIView

from products.models import Product
from products.api_endpoints.ProductCreate.serializers import ProductCreateSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = []
