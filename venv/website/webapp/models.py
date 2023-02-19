from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=20, default="")
    company = models.CharField(max_length=20, default="")
    salary = models.CharField(max_length=20, default="")
    location = models.CharField(max_length=20, default="")
    url = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=1000, default="")
