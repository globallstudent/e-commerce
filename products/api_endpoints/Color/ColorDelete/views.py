from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import Color


class ColorDeleteAPIView(DestroyAPIView):
    queryset = Color.objects.all()
    permission_classes = [permissions.IsAuthenticated]
