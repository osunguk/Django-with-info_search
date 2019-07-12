from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('processing', views.processing, name="processing"),
    path('indexing', views.indexing, name="indexing"),
    path('token', views.token,name="token"),
    path('normalization', views.normalization,name="normalization"),
    path('stop_word', views.stop_word,name="stop_word"),
    path('mkdic', views.mkdic,name="mkdic"),
    path('tf', views.tf,name="tf"),
    path('df', views.df,name="df"),
    path('idf', views.idf,name="idf")
]
