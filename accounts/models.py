from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import BaseModel

class User(models.Model):
