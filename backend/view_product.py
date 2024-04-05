from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from backend.models import Product
from backend.serializers import ProductViewSerializer


class productListView(ListAPIView):
    serializer_class = ProductViewSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        if id is not None:
            return Product.objects.filter(id=id)
        return Product.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)