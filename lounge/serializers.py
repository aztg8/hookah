from rest_framework import serializers
from lounge.models import *
from common.serializers import MediaURLSerializer


class MetroSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class LoungeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lounge
        fields = "__all__"
        read_only_fields = [fields]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('title', 'url')
        read_only_fields = fields


class LoungePhotoSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()

    class Meta:
        model = LoungePhoto
        fields = "__all__"
        read_only_fields = [fields]
