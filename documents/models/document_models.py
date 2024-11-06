from django.db import models
from employee.models.employe_models import EmployeModels
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class DocumentModels(NamedDateTimeModel):
    employe = models.ForeignKey(EmployeModels, on_delete=models.CASCADE, related_name='documents')
    type_document = models.CharField(max_length=255)
    url_file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
