from rest_framework import serializers
from documents.models.newsletter_models import NewsletterModels


class NewsletterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsletterModels
        fields = "__all__"
