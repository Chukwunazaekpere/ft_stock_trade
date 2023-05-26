from django.db.models.query_utils import Q
from rest_framework import viewsets
from django.template.loader import render_to_string

from rest_framework.response import Response
from .models import (
    Users,
)
from django.contrib.auth import authenticate, login

from django.core.mail import send_mail
from .serializers import ( 
    UserSerializer,
    LoginSerializer,
)

from rest_framework.decorators import action
from django.shortcuts import redirect
from rest_framework import status


class UsersViewSets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = []       

    @action(methods=['POST'], detail=False, url_path='register')
    def register(self, *args, **kwargs):
        try:
            users_data = self.request.data['data']
            serializer = UserSerializer(data=users_data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                password = validated_data['password']
                email = Users.normalize_username(validated_data['email'])
                new_user = Users()
                new_user.firstname = validated_data['firstname'],
                new_user.set_password(password)
                new_user.lastname = validated_data['lastname'],
                new_user.email = email,
                new_user.phone = validated_data['phone'],
                new_user.address = validated_data['address'],
                new_user.save(*args, **kwargs)
                return Response(data="Successful", status=status.HTTP_201_CREATED, content_type="application/json")
            raise Exception(serializer.errors)
        except:
            error = serializer.errors
            print("\n\t Errors: ",error)
            return Response(data=error, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')


    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, *args, **kwargs):
        login_details = self.request.data['data']
        try:
            serializer = LoginSerializer(data=login_details)
            if serializer.is_valid():
               

                if check_password:
                    login(self.request, related_user)
                    users_details = {
                        "status":"Login Successful", 
                        "user": related_users_name, 
                        "user_mode": related_user.user_mode, 
                        "profile_pics": related_user.profile_image or ""
                    }
                    return Response(data=users_details, status=status.HTTP_200_OK, content_type='application/json')
                return Response(data="Invalid Login Credentials", status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        except Exception as error:
            print("\n\t Error: ", error)
            return Response(data="Invalid Login Credentials", status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
