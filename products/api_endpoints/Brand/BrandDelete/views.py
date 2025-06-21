from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import Brand


class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAuthenticated]
