from django.urls import path

from lounge.views import *

urlpatterns = [
    path("metro/", MetroListAPIView.as_view(), name="metro"),
    path("lounge/", LoungeListAPIView.as_view(), name="lounge"),
    path("address/", AddressAPIView.as_view(), name="address"),
    path("lounge_photo/", LoungePhotoAPIView.as_view(), name="lounge-photo"),
]
