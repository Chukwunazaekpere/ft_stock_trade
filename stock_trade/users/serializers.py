from django.db import models
from rest_framework import fields, serializers
from .models import (
    Users
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["firstname", "lastname", "email", "phone", "address", "password"]

    def validate(self, attrs):
        super().validate(attrs)
        if len(attrs["phone"]) < 11:
            raise serializers.ValidationError("Phone number musst be greater than 11")
        elif len(attrs["password"]) < 8:
            raise serializers.ValidationError("Password lenght must be greater than seven characters")
        elif attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password and confirm-password fields must be the same")
        return attrs



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', "password"]

    def validate(self, attrs):
        super().validate(attrs)
        login_email = attrs['email'].lower()  # normalize the email
        login_password = attrs['password']
        #  Check if the login - email exists
        related_user: Users = Users.find_one(attr="email", val=login_email)
        if related_user:
            check_password = related_user.check_password(login_password)
        
    
        
