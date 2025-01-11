from rest_framework import serializers

from apps.core.api.serializers import BaseSerializer


class LLMRequestSerializer(BaseSerializer):
    text = serializers.CharField(max_length=120)


class AppAttrsSerializer(BaseSerializer):
    name = serializers.CharField(max_length=60, allow_null=True)
    params = serializers.DictField(default=dict())

class LLMResponseSerializer(BaseSerializer):
    message = serializers.CharField(max_length=500)
    app = AppAttrsSerializer()

