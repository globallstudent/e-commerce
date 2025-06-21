from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from products.models import Size
from products.api_endpoints.Size.SizeCreate.serializers import SizeCreateSerializer


class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
