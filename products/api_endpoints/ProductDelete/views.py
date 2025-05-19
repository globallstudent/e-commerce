from rest_framework.generics import DestroyAPIView

from products.models import Product


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = []
    lookup_field = 'pk'
