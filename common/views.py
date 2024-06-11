from rest_framework.generics import ListAPIView, CreateAPIView

from common.models import *
from common.serializers import *


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FeedbackListAPIView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer
