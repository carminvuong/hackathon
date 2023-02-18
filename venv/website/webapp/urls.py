from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('find_job/', views.find_job)
]
