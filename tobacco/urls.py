from django.urls import path
from tobacco.views import *

urlpatterns = [
    path("manufacturer/", ManufacturerListAPIView.as_view(), name="manufacturer"),
    path("country/", CountryListAPIView.as_view(), name="country"),
    path("prep_method/", PrepMethodListAPIView.as_view(), name="prep_method"),
    path("product/", ProductListAPIView.as_view(), name="product")
]
