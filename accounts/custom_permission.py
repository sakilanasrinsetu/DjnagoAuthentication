from django.db.models import Q
from accounts.models import Student
from rest_framework import permissions
from django.contrib.auth.models import User

class IsTeacher(permissions.BasePermission):
    message = ' You are Not a Teacher'
    def has_permission(self, request, view):
        if not bool(request.user and request.user.is_authenticated):
            return False
        # request.user.get_user_permissions()
        teacher_qs = User.objects.all()