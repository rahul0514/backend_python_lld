from rest_framework.generics import ListCreateAPIView

from ecom.models import Product
from ecom.serializer import ProductSerializer

from rest_framework.permissions import IsAuthenticated


# def say_hello(request):
#     print("This is with in View")
#     return HttpResponse('Hello from scaler!')

class EmptyException(Exception):
    pass


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]  # this line of code ask for tokens  #comment for exception testing


class ProductListAPIView(ListCreateAPIView):
    def get_queryset(self):
        product = Product.objects.all()

        if len(product) == 0:
            raise EmptyException()

        return ProductSerializer(product, many=True)
