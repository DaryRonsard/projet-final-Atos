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


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # def put(self, request):
    #
    #     user = request.user
    #
    #     new_password = request.data.get('new_password')
    #     confirm_password = request.data.get('confirm_password')
    #
    #
    #     if new_password != confirm_password:
    #         return Response(
    #             {"error": "Les mots de passe ne correspondent pas."},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #
    #     user.set_password(new_password)
    #     user.save()
    #
    #     return Response(
    #         {"detail": "Le mot de passe a été mis à jour avec succès."},
    #         status=status.HTTP_200_OK
    #     )

    #permission_classes = [IsAuthenticated]
    # def put(self, request):
    #
    #     user = request.user
    #
    #     new_password = request.data.get('new_password')
    #     confirm_password = request.data.get('confirm_password')
    #
    #
    #     if new_password != confirm_password:
    #         return Response(
    #             {"error": "Les mots de passe ne correspondent pas."},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #
    #     user.set_password(new_password)
    #     user.save()
    #
    #     return Response(
    #         {"detail": "Le mot de passe a été mis à jour avec succès."},
    #         status=status.HTTP_200_OK
    #     )


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = UserModels.objects.all()
#
#     # hacher le mots de passe lors de la creations
#     @action(detail=False, methods=['post'])
#     def create_crypt_and_password(self, request, pk=None):
#         data = JSONParser().parse(request)
#         password = data['password']
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save(password=make_password(password))
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)