from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tf', views.tf),
    path('df', views.df),
    path('idf', views.idf)
]
