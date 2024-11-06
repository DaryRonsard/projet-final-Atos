from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models.helpers.date_time_model import DateTimeModel
from rest_framework.authtoken.models import Token
from django.conf import settings

ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('employee', 'Employee'),
    )


class UserModels(DateTimeModel, AbstractUser):
    role = models.CharField(max_length=13, choices=ROLE_CHOICES )
    profil_image = models.ImageField(upload_to='profiles/', blank=True, null=True)


    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

