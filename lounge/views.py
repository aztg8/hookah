from rest_framework.generics import ListAPIView, RetrieveAPIView

from lounge.models import *
from lounge.serializers import *


class MetroListAPIView(ListAPIView):
    queryset = Metro.objects.all()
    serializer_class = MetroSerializer


class LoungeListAPIView(ListAPIView):
    queryset = Lounge.objects.all()
    serializer_class = LoungeSerializer


class AddressAPIView(RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class LoungePhotoAPIView(ListAPIView):
    queryset = LoungePhoto.objects.all()
    serializer_class = LoungePhotoSerializer
