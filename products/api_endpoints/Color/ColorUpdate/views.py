from rest_framework.generics import UpdateAPIView
from rest_framework import permissions

from products.models import Color
from products.api_endpoints.Color.ColorUpdate.serializers import ColorUpdateSerializer


class ColorUpdateAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
