from django.db import models
from django.contrib.auth.models import(
  AbstractBaseUser, PermissionsMixin
)
from datetime import datetime, timedelta
from django.contrib.auth.models import UserManager

class Users(AbstractBaseUser,PermissionsMixin):
  username = models.CharField(max_length=255)
  age = models.PositiveBigIntegerField()
  email = models.EmailField(max_length=255,unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  picture = models.FileField(null=True,upload_to='picture')

  objects = UserManager() #ログイン・ログアウト処理にはUserManagerが必要

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username','age']

  class Meta:
    db_table= 'users'

