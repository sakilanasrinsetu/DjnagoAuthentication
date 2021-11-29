from django.shortcuts import render

from auth import settings
from .models import Student
from .serializers import StudentSerializer, LoginUserSerializer
from rest_framework import viewsets, permissions
from utils.response_wrapper import ResponseWrapper
from utils.custom_viewset import CustomViewSet

# from utils.custom_permission import IsTeacher
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, AllowAny,IsAdminUser
from . import custom_permission as custom_permissions
from rest_auth.models import TokenModel
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView

from rest_auth.app_settings import (
    TokenSerializer, UserDetailsSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer, JWTSerializer, create_token
)
from rest_auth.utils import jwt_encode
# Create your views here.

class StudentViewSet(CustomViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'pk'
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action in ['post']:
            permission_classes = [AllowAny]
        elif self.action in ['list']:
            permission_classes=[
                custom_permissions.IsTeacher
            ]
        return [permission() for permission in permission_classes]

# class LoginViewSet(viewsets.ViewSet):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginUserSerializer
#     token_model = TokenModel
#
#     def login(self):
#         self.email = self.serializer.validated_data['email']
#
#         if getattr(settings, 'REST_USE_JWT', False):
#             self.token = jwt_encode(self.user)
#         else:
#             self.token = create_token(self.token_model, self.user,
#                                       self.serializer)
#
#         if getattr(settings, 'REST_SESSION_LOGIN', True):
#             self.process_login()