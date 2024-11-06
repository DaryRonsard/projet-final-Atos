from rest_framework import viewsets

from employee.models.direction_models import DirectionModels
from employee.serializers.direction_serializer import DirectionSerializer


class DirectionViewSet(viewsets.ModelViewSet):
    serializer_class = DirectionSerializer
    queryset = DirectionModels.objects.all()
