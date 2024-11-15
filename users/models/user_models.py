from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models.helpers.date_time_model import DateTimeModel
from rest_framework.authtoken.models import Token
from django.conf import settings


class UserModels(DateTimeModel, AbstractUser):
    ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('employee', 'Employee'),
    )

    role = models.CharField(max_length=13, choices=ROLE_CHOICES )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    #profil_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

