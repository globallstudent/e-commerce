from rest_framework.generics import CreateAPIView

from products.models import Size
from products.api_endpoints.SizeCreate.serializers import SizeCreateSerializer


class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeCreateSerializer
    permission_classes = []
