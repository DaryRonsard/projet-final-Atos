from django.db import models
from users.models.user_models import UserModels


class NewsletterModels(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    admin_rh = models.ForeignKey(UserModels, on_delete=models.CASCADE, related_name='newsletters')

    def __str__(self):
        return self.titre