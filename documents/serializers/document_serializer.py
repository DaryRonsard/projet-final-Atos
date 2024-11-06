from rest_framework import serializers
from documents.models.document_models import DocumentModels


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentModels
        fields = "__all__"
