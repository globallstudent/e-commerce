from rest_framework.generics import DestroyAPIView

from products.models import Brand


class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    permission_classes = []
    lookup_field = 'pk'
