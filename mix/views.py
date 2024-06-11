from rest_framework.generics import ListAPIView, RetrieveAPIView

from mix.models import *
from mix.serializers import *


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class VariantsListAPIView(ListAPIView):
    queryset = Variants.objects.all()
    serializer_class = VariantsSerializer


class MixListAPIView(ListAPIView):
    queryset = Mix.objects.all()
    serializer_class = MixSerializer


class MixPartAPIView(ListAPIView):
    queryset = MixPart.objects.all()
    serializer_class = MixPartSerializer

