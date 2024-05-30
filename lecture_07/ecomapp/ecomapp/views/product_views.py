from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ecomapp.models import Product, DiaryProduct
from ecomapp.serializers import ProductSerializer, DiaryProductSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateProductAPIView(GenericAPIView):

    def get(self, request):
        products = Product.objects.all().filter(price__lte=100) # __gte, __in=[100.0, 70.0], filter is sending list

        # products = Product.objects.raw('SELECT * FROM ecomapp product where price BETWEEN 70.0 and 100.0') #Not work

        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data, status=200)

    def post(self, request):
        data = request.data
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response(decoded_data.errors, status=404)
        decoded_data.save()
        return Response(decoded_data.data, status=201)


class DiaryListCreateAPIView(ListCreateAPIView):
    queryset = DiaryProduct.objects.all()
    serializer_class = DiaryProductSerializer


class DiaryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DiaryProduct.objects.all()
    serializer_class = DiaryProductSerializer
