from users.models.user_models import UserModels
from rest_framework.serializers import ModelSerializer


class PasswordSerializer(ModelSerializer):

    class Meta:
        model = UserModels
        fields = ["password"]