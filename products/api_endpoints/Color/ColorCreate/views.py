from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from products.models import Color
from products.api_endpoints.Color.ColorCreate.serializers import ColorCreateSerializer


class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
