from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=40)
    cc = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = ["email"]
    REQUIRED_FIELDS = []

    


