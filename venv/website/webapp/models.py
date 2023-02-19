from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, default="")
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)


class Job(models.Model):
    title = models.CharField(max_length=20, default="")
    company = models.CharField(max_length=20, default="")
    salary = models.CharField(max_length=20, default="")
    location = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=100, default="")
