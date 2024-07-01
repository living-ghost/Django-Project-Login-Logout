from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Add any additional fields you want
    pass

class User(models.Model):
    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=200, null=False)

class Admin(models.Model):
    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(max_length=200, unique=True, null=False)
    password = models.CharField(max_length=200, null=False)