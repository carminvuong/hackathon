from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, "webapp/home.html")


def find_job(request):
    return render(request, "webapp/find_job.html")
