from rest_framework.generics import ListAPIView
from rest_framework import permissions

from products.models import Color
from products.api_endpoints.Color.ColorList.serializers import ColorListSerializer


class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorListSerializer
    permission_classes = [permissions.IsAuthenticated]
