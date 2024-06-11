from django.urls import path
from mix.views import *

urlpatterns = [
    path("tags/", TagListAPIView.as_view(), name="tags"),
    path("variants/", VariantsListAPIView.as_view(), name="variants"),
    path("mix/", MixListAPIView.as_view(), name="mix"),
    path("mix_part/", MixPartAPIView.as_view(), name="mix-part"),
]
