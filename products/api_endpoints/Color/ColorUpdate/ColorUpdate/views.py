from rest_framework.generics import UpdateAPIView

from products.models import Color
from products.api_endpoints.ColorUpdate.serializers import ColorUpdateSerializer


class ColorUpdateAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorUpdateSerializer
    permission_classes = []
    lookup_field = 'pk'
