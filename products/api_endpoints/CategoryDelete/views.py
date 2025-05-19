from rest_framework.generics import DestroyAPIView

from products.models import Category


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = []
    lookup_field = 'pk'
