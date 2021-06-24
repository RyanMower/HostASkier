from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django import forms
from urllib.parse import urlencode
from phonenumber_field.modelfields import PhoneNumberField
import yaml
import requests

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, 
            first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email.")
        if not username:
            raise ValueError("Users must have a username.")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name, 
            phone_number = phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username     = username,
            password     = password,
            first_name   = 'admin',
            last_name    = 'admin',
            phone_number = 'admin'
        )

        user.is_admin     = True
        user.is_staff     = True
        user.is_active    = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email        = models.EmailField(unique=True)
    username     = models.CharField(max_length=30, unique=True)
    date_joined  = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login   = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    ## My Fields ##
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)       
    phone_number = PhoneNumberField(verbose_name="Phone Number", null=False)
    approved = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_laber):
        return True

    def save(self, **kwargs):
        super().save(**kwargs)

