from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets, permissions
from utils.response_wrapper import ResponseWrapper
from utils.custom_viewset import CustomViewSet

# from utils.custom_permission import IsTeacher
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, AllowAny,IsAdminUser
from . import custom_permission as custom_permissions
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
