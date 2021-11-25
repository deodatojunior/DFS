from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('erro/', views.erro, name='erro'),
    path('ativar_camera/', views.ativar_camera, name="ativar_camera")
]
