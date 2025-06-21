from rest_framework.generics import DestroyAPIView

from products.models import Size


class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    permission_classes = []
    lookup_field = 'pk'
