from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('findJob/', views.findJob),
    path('results/', views.results),
    path('favorites/', views.favorites),
    path('moreInfo/', views.moreInfo)
]
