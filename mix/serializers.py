from rest_framework import serializers
from mix.models import *


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class VariantsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class MixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mix
        fields = "__all__"
        read_only_fields = [fields]


class MixPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MixPart
        fields = "__all__"
        read_only_fields = [fields]

