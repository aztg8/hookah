from rest_framework import serializers
from tobacco.models import *
from common.serializers import MediaURLSerializer


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class PrepMethodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = [fields]
