from rest_framework import serializers

from apps.core.api.serializers import BaseSerializer


class AssistanceSerializer(BaseSerializer):
    user_speech = serializers.CharField(max_length=120)
