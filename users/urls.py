"""
URL configuration for e_com project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

from users.viewset.user_viewset import UserRegistrationView, UserViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
# router.register(r'register-user', UserRegistrationView, basename='register-user')
# router.register(r'update-password', UserUpdatePasswordView, basename='update-password')

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@gsnippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


app_name = 'users'


urlpatterns = [
    path('', include(router.urls)),
    path('create-user/', UserRegistrationView.as_view(), name='register-user'),
    #path('update-password/', UserUpdatePasswordView.as_view(), name='update-password'),
]