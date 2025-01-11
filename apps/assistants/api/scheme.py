from drf_spectacular.utils import extend_schema, extend_schema_view

from . import serializers, views

extend_schema_view(
    ask_kapi=extend_schema(
        request=serializers.LLMRequestSerializer,
        responses=serializers.LLMResponseSerializer,
    ),
)(views.AssistanceViewSet)
