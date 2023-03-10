from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="")
    company = models.CharField(max_length=200, default="")
    salary = models.CharField(max_length=200, default="")
    location = models.CharField(max_length=200, default="")
    url = models.CharField(max_length=1000, default="")
    description = models.CharField(max_length=5000, default="")
    fullDescription = models.CharField(
        max_length=50000, default="")
    favorite = models.BooleanField(default=False)
