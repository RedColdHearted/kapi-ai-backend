from rest_framework import status
from rest_framework.response import Response

from apps.core.api.views import BaseViewSet

from .serializers import AssistanceSerializer


class AssistanceViewSet(BaseViewSet):
    """."""
    serializer_class = AssistanceSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        return (Response(data=, status=status.HTTP_201_CREATED))
