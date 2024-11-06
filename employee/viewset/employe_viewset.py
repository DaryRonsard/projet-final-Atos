from rest_framework import viewsets

from employee.models.employe_models import EmployeModels
from employee.serializers.employe_serializer import EmployeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeSerializer
    queryset = EmployeModels.objects.all()


