from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import serializers, status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import Token
from rest_framework.authtoken.models import Token

from users.models.user_models import UserModels
from users.serializers.password_serializer import PasswordSerializer
from users.serializers.user_serializer import UserSerializer
from users.serializers.user_and_employé_register import UserEmployeeRegisterSerializer



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModels.objects.all()

    @action(detail=False, methods=['post'])
    def create_crypt_and_password(self, request, pk=None):
        data = JSONParser().parse(request)
        password = data['password']
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save(password=make_password(password))
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    # @action(detail=False, methods=['post'])
    @action(detail=True, methods=['put'], url_path='change_password')
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            new_password = serializer.validated_data['password']
            user.password = make_password(new_password)
            user.save()
            return Response({'detail': 'Mot de passe changé avec succès !'}, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEmployeeRegisterView(APIView):
    def post(self, request):
        serializer = UserEmployeeRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Utilisateur et employé créés avec succès.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)