from rest_framework.generics import ListAPIView

from tobacco.models import *
from tobacco.serializers import *


class ManufacturerListAPIView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class PrepMethodListAPIView(ListAPIView):
    queryset = PrepMethod.objects.all()
    serializer_class = PrepMethodSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



