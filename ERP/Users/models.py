# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
import uuid
import datetime

#Handle User model 
class UserManager(models.Manager):
    print("SII")

#Handle model LogUser model
class LogUserManager(models.Manager):
    print("SII")

#Handle model Token model
class AuthTokenManager(models.Manager):
    print("SII")

#Handle model Role model
class RoleManager(models.Manager):
    print("SII")

#Create User model
class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=240, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
    objects = UserManager()
    def __str__(self):
        return self.user_name

#Create Log_User model
class LogUser(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    objects = LogUserManager()

#Create Token model
class Token(models.Model):
    token = models.CharField(max_length=254, unique=True)
    date_created = models.DateField(auto_now=True)
    last_activation = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = AuthTokenManager()

#Create Role  model
class Role(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    objects = RoleManager()
    