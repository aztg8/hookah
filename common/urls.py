from django.urls import path

from common.views import *

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="users"),
    path("feedback/", FeedbackListAPIView.as_view(), name="feedback")
]