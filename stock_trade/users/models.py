from typing import Optional
# from djongo import models
from django.db import models

from django.conf import settings


# from stock_trade.config.db_config import db_config
# from ..stock_trade.config.db_config import db_config
from datetime import datetime
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


class BaseUserModelManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, phone, password, **kwargs):
        try:
            if not firstname:
                raise ValueError("Firstname is required.")
            if not lastname:
                raise ValueError("Lastname is required.")
            if not email:
                raise ValueError("Email is required")
            
            email = self.normalize_email(email)
            new_user = self.model(firstname=firstname, lastname=lastname, email=email, phone=phone, **kwargs)
            new_user.set_password(password)
            new_user.save(using=self._db)
            return new_user
        except Exception as error:
            print("\n\t Create user error: ", error)
            return error

    def create_superuser(self, email, firstname, lastname, password, **kwargs):
        try:
            kwargs.setdefault("is_active", True)
            kwargs.setdefault("is_staff", True)
            kwargs.setdefault("is_superuser", True)

            new_superuser = self.create_user(
                email=email,
                firstname=firstname,
                lastname=lastname,
                password=password,
                **kwargs
            )
            return new_superuser
        except Exception as error:
            return error



class Users(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=150)
    date_registered = models.DateTimeField(verbose_name="Date of Registration", auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, help_text="Whether this user is active or not")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = BaseUserModelManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone']

    def users_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    @classmethod
    def get_user_by_id(self, users_id):
        user = self.objects.filter(pk=users_id)
        print("\n\t User_by_id: ", user)
        return user

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
    

        
        
    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"


