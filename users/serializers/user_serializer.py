from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models.user_models import UserModels


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModels
        fields = "__all__ "
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModels(**validated_data)
        user.set_password(password)
        user.save()
        return user

    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #
    #     if password:
    #         instance.set_password(password)
    #
    #     instance.save()
    #     return instance




