from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
]
