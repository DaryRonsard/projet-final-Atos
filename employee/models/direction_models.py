from django.db import models
from employee.models.employe_models import EmployeModels
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class DirectionModels(NamedDateTimeModel):
    description = models.TextField()
    employe_chef = models.ForeignKey(EmployeModels, on_delete=models.CASCADE, related_name='directions')

    def __str__(self):
        return self.name