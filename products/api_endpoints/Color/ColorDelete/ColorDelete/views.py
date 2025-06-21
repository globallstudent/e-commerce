from rest_framework.generics import DestroyAPIView

from products.models import Color


class ColorDeleteAPIView(DestroyAPIView):
    queryset = Color.objects.all()
    permission_classes = []
    lookup_field = 'pk'
