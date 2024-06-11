from rest_framework import serializers
from common.models import *


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None
        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except:
            return "http://testserver" + str(media.file.url)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class FeedbackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('author_id', 'created_at', 'stars', 'text')
        read_only_fields = fields
