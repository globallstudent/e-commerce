from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import Size


class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
