from django.db import models
from datetime import datetime
from base.models.helpers.date_time_model import DateTimeModel
from django.conf import settings


class EmployeModels(DateTimeModel):
    GENRE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    ]

    TYPE_DE_CONTRAT = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('STAGE', 'STAGE'),
        ('TEMPLATE_PARTIEL', 'TEMPLATE_PARTIEL'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=60)
    # last_name = models.CharField(max_length=60)
    sexe = models.CharField(max_length=50, choices=GENRE)
    contrat = models.CharField(max_length=50, choices=TYPE_DE_CONTRAT)
    matricule = models.CharField(max_length=6)
    salaire = models.CharField(max_length=60)
    date_embauche = models.DateField(default=datetime(2024, 1, 1))
    department = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='media/', null=True, blank=True)
    social_secure_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"