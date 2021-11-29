import asyncio
from .models import Student
from rest_framework import serializers
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LoginUserSerializer(serializers.ModelSerializer):
    user= serializers.SerializerMethodField(required=False)

    class Meta:
        model = User
        fields =['email','password','user']
        # fields ='__all__'

    def get_user(self,obj):
        if obj:
            email = User.objects.filter(email= obj.email).last()
            return 'username'
        return {}



